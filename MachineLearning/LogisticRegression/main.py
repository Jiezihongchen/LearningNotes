import torch
import torch.nn as nn
from torch.autograd import Variable
import torchvision.transforms as transform
import torch.utils.data as Data
import torch.optim as optim
import torchvision.datasets as dsets

# steps:
# 1. load dataset
# 2. make dataset iterable
# 3. create model
# 4. create loss function
# 5. create optimizer
# 6. train


class LogisticRegression(nn.Module):
    def __init__(self, n_input, n_output):
        super(LogisticRegression, self).__init__()
        self.linear = nn.Linear(n_input, n_output)

    def forward(self, x):
        return self.linear(x)


if __name__ == "__main__":
    # load dataset
    train_df = dsets.MNIST(
        root="./data",
        train=True,
        transform=transform.ToTensor(),
        download=False)
    test_df = dsets.MNIST(
        root="./data",
        train=False,
        transform=transform.ToTensor())

    # parameter setting
    batch_size = 128
    n_iteration = 4096
    learning_rate = 0.03
    n_input = 784
    n_output = 10
    epochs = n_iteration / (len(train_df) / batch_size)
    # logistic regression model
    lr_model = LogisticRegression(n_input, n_output)

    # make dataset iterable
    train_loader = Data.DataLoader(
        dataset=train_df,
        batch_size=batch_size,
        shuffle=True)
    test_loader = Data.DataLoader(
        dataset=test_df,
        batch_size=batch_size,
        shuffle=True)

    # loss_function
    loss_function = nn.CrossEntropyLoss()
    # optimizer
    optimizer = optim.SGD(lr_model.parameters(), lr=learning_rate)

    # train model
    for i in range(int(epochs)):
        for idx, (image, label) in enumerate(train_loader):
            image = Variable(image.view(-1, 28 * 28))
            label = Variable(label)
