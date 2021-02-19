import numpy as np
import pandas as pd
import random

from sklearn.model_selection import KFold
from sklearn.metrics import roc_auc_score

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
import torch.optim as optim
import copy


class TorchFM(nn.Module):
    def __init__(self, n=None, k=None):
        super(TorchFM, self).__init__()
        # n: number of feature
        # k: length of latent vector
        self.V = nn.Parameter(torch.randn(n, k), requires_grad=True)
        self.w = nn.Linear(n, 1, bias=True)

    def forward(self, x):
        out_1 = torch.matmul(x, self.V).pow(2).sum(1, keepdim=True)
        out_2 = torch.matmul(x.pow(2), self.V.pow(2)).sum(1, keepdim=True)

        out_inter = 0.5 * (out_1 - out_2)
        out_linear = self.w(x)
        out = out_linear + out_inter

        return out


def sigmoid(x):
    return 1 / (np.exp(-x) + 1)


def load_data():
    file_path = "dota_train_binary_heroes/"
    train_name = "dota_train_binary_heroes.csv"
    test_name = "dota_test_binary_heroes.csv"
    target_name = "train_targets.csv"

    train_df = pd.read_csv(file_path + train_name, index_col="match_id_hash")
    train_df = train_df.values.astype(np.float32)

    test_df = pd.read_csv(file_path + test_name, index_col="match_id_hash")
    test_df = test_df.values.astype(np.float32)

    target_df = pd.read_csv(file_path + target_name, index_col="match_id_hash")
    y = target_df["radiant_win"].values.astype(np.float32)
    y = y.reshape(-1, 1)

    return train_df, test_df, y


def train_model(X_train, X_test, y):
    train_tensor = torch.from_numpy(X_train)
    test_tensor = torch.from_numpy(X_test)
    y_tensor = torch.from_numpy(y)

    n_feature = X_train.shape[1]
    k = 3
    fm_model = TorchFM(n_feature, k)
    loss_fnc = nn.BCEWithLogitsLoss()
    optimizer = optim.SGD(fm_model.parameters(), lr=0.03, weight_decay=0.007)

    folds = KFold(n_splits=7)
    n_iteration = 512
    batch_size = 2 << 8
    epochs = int(n_iteration / (X_train.shape[0] / batch_size))

    models = []
    scores = []

    train_pred = np.zeros(y.shape)
    test_pred = np.zeros((X_test.shape[0], 1))

    for n_fold, (train_ind, valid_ind) in enumerate(folds.split(X_train, y)):
        print("Fold %d:" % (n_fold + 1))
        train_set = TensorDataset(train_tensor[train_ind], y_tensor[train_ind])
        valid_set = TensorDataset(train_tensor[valid_ind], y_tensor[valid_ind])

        loaders = {
            "train": DataLoader(
                train_set,
                batch_size=batch_size,
                shuffle=True),
            "valid": DataLoader(
                valid_set,
                batch_size=batch_size,
                shuffle=False)}

        best_score = -1
        best_model_wts = copy.deepcopy(fm_model.state_dict())

        for epoch in range(epochs):
            loss_score = {"train": 0, "valid": 0}
            for phase in ["train", "valid"]:
                if phase == "train":
                    fm_model.train()
                else:
                    fm_model.eval()

                for batch_x, batch_y in loaders[phase]:
                    optimizer.zero_grad()
                    out = fm_model(batch_x)
                    loss = loss_fnc(out, batch_y)
                    loss_score[phase] += loss.item() * batch_x.size(0)

                    with torch.set_grad_enabled(phase == "train"):
                        if phase == "train":
                            loss.backward()
                            optimizer.step()
                loss_score[phase] /= len(loaders[phase].dataset)

            epoch_score = -1
            with torch.no_grad():
                fm_model.eval()
                valid_pred = sigmoid(fm_model(train_tensor[valid_ind]).numpy())
                epoch_score = roc_auc_score(y_tensor[valid_ind], valid_pred)
                if epoch_score > best_score:
                    best_score = epoch_score
                    best_model_wts = (fm_model.state_dict())

            if (epoch + 1) % 5 == 0:
                print(
                    f"epoch {epoch + 1}: train loss: {loss_score['train']:.3f}, "
                    f"valid loss: {loss_score['valid']:.3f},"
                    f"roc_auc_score: {epoch_score:.3f}")

        with torch.no_grad():
            fm_model.load_state_dict(best_model_wts)
            fm_model.eval()

            train_pred[valid_ind] = sigmoid(
                fm_model(train_tensor[valid_ind]).numpy())
            fold_score = roc_auc_score(y[valid_ind], train_pred[valid_ind])
            scores.append(fold_score)
            models.append(fm_model)

            print(f"BEST_ROC_AUC SCORE {fold_score:.3f}")

            test_pred += sigmoid(fm_model(test_tensor).numpy())

    test_pred /= folds.n_splits
    return models, train_pred, test_pred


if __name__ == "__main__":
    train_df, test_df, y = load_data()
    models, trian_pred, test_pred = train_model(train_df, test_df, y)
