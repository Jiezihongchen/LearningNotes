import torch
import torch.nn as nn
import torch.optim as optim


class TorchFM(nn.Module):
    def __init__(self, n=None, k=None):
        super().__init__()
        # n: 特征数 k: 隐向量长度
        self.V = nn.Parameter(torch.randn(n, k), requires_grad=True)
        #
        self.lin = nn.Linear(n, 1)

    def forward(self, x):
        # 计算s1
        s1 = torch.matmul(x, self.V)
        s1 = torch.pow(s1)
        s1 = torch.sum(input=s1, dim=1, keepdim=True)
        # 计算s2
        s2 = torch.matmul(torch.pow(x), torch.pow(self.V))
        s2 = torch.sum(input=s2, dim=1, keepdim=True)

        y_i = self.lin(x)
        y_ij = 0.5 * (s1 - s2)
        out = y_i + y_ij

        return out

def train_model():
    # todo
    optimizer = optim.SGD()

if __name__ == "__main__":
    pass
