import torch
import torch.nn as nn
import torch.nn.functional as F

class FCN(nn.Module):
    def __init__(self):
        super(FCN, self).__init__()
        self.fc1 = nn.Linear(2, 10)
        self.fc2 = nn.Linear(10, 1)
        self.out = nn.Sigmoid()

    def forward(self, x):
        x = torch.flatten(x)
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.out(x)

        return x