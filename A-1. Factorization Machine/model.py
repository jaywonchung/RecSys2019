import torch
import torch.nn as nn

from constants import *

def FM(nn.Module):

    def __init__(self, d, session_dim, item_dim):
        super.__init__()

        Q = torch.zeros(session_dim, d).random_(0, 1)
        P = torch.zeros(item_dim, d).random_(0, 1)
        bq = torch.zeros(session_dim).random_(0, 1)
        bp = torch.zeros(item_dim).random_(0, 1)

    def forward(self, s, i):
        """
        s has size [batch_size, session_dim]
        i has size [batch_size, item_dim]

        output has size [batch_size, 1]
        """
        return torch.sum(torch.matmul(s, Q) * torch.matmul(i, P) + s * bq + i * bp, dim=1)
