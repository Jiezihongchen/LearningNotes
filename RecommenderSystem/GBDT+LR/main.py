import numpy as np
import pandas as pd

from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

import lightgbm as lgb
import os


def load_data():
    print("Load dataset")
    index_name = "match_id_hash"

    root_path = "../../dataset/dota_train_binary_heroes/"
    data_path = root_path + "dota_train_binary_heroes.csv"
    target_path = root_path + "train_targets.csv"

    data = pd.read_csv(data_path, index_col=index_name)
    target = pd.read_csv(target_path, index_col=index_name)
    target = target["radiant_win"].values.astype(np.int)

    X_train, X_test, y_train, y_test = train_test_split(
        data, target, test_size=0.3, random_state=42)
    col_name = data.columns

    return X_train, X_test, y_train, y_test, col_name


def build_feature(X_train, X_test, y_train, y_test, col_name):
    print("Build Tree")
    lgb_train = lgb.Dataset(X_train, y_train)
    lgb_test = lgb.Dataset(X_test, y_test, reference=lgb_train)

    params = {
        "task": "train",
        "boosting_type": "gbdt",
        "objective": "binary",
        'metric': {'binary_logloss'},
        "num_leaves": 32,
        "num_trees": 64,
        "learning_rate": 0.03,
        'feature_fraction': 0.9,
        'bagging_fraction': 0.8,
        'bagging_freq': 5,
        'verbose': 0
    }

    gbm = lgb.train(
        params,
        lgb_train,
        num_boost_round=64,
        valid_sets=lgb_train)
    gbm.save_model("model.txt")

    y_pred = gbm.predict(X_train, pred_leaf=True)

    print("Build features")
    num_leaves = 64
    col_length = y_pred.shape[1] * num_leaves
    transformed_training_matrix = np.zeros(
        [y_pred.shape[0], col_length], dtype=np.int)

    for idx in range(len(y_pred)):
        for i in range(len(y_pred[idx])):
            transformed_training_matrix[idx][i *
                                             num_leaves + y_pred[idx][i]] += 1

    y_pred = gbm.predict(X_test, pred_leaf=True)
    transformed_test_matrix = np.zeros(
        [y_pred.shape[0], col_length], dtype=np.int)
    for idx in range(len(y_pred)):
        for i in range(len(y_pred[idx])):
            transformed_test_matrix[idx][i * num_leaves + y_pred[idx][i]] += 1

    print("Build logistic regression")
    lr = LogisticRegression(penalty="l2", C=0.08)
    lr.fit(transformed_training_matrix, y_train)
    y_pred = lr.predict_proba(transformed_test_matrix)
    print(y_pred)

    normalized_cross_entropy = (-1 / y_pred.shape[0]) * sum((((1 + y_test) / 2) * np.log(
        y_pred[:, 1])) + ((1 - y_test) / 2) * np.log(1 - y_pred[:, 1]))
    print("Normalized Cross Entropy: " + str(normalized_cross_entropy))


if __name__ == "__main__":
    X_train, X_test, y_train, y_test, col_name = load_data()
    build_feature(X_train, X_test, y_train, y_test, col_name)
