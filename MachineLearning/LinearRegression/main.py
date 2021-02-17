import torch
import torch.nn as nn
import torch.utils.data as Data
import torch.optim as optim
from sklearn.datasets import make_regression
import numpy as np

if __name__ == "__main__":
    # generate data
    n_samples = 256
    n_features = 2
    X, y = make_regression(n_samples=n_samples, n_features=n_features,
                           n_informative=n_features, n_targets=1, bias=0.3, noise=0.03)
    X = torch.from_numpy(X).to(torch.float32)
    y = torch.from_numpy(y).to(torch.float32)

    batch_size = 2 << 4
    n_epochs = 4

    dataset = Data.TensorDataset(X, y)
    data_iter = Data.DataLoader(dataset, batch_size, shuffle=True)

    linear_model = nn.Sequential(
        nn.Linear(n_features, 1)
    )
    nn.init.normal_(linear_model[0].weight, mean=0, std=0.3)
    nn.init.constant_(linear_model[0].bias, val=0)
    loss = nn.MSELoss()
    optimizer = optim.SGD(linear_model.parameters(), lr=0.03)

    for epoch in range(1, n_epochs + 1):
        for X, y in data_iter:
            output = linear_model(X)
            l = loss(output, y.view(-1, 1))
            optimizer.zero_grad()
            l.backward()
            optimizer.step()
        print("epoch %d, loss: %f" % (epoch, l.item()))
