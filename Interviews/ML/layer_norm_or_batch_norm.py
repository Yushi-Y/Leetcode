### Numpy solution

import numpy as np

def batch_norm(X, gamma, beta, eps=1e-5):
    """
    X: (batch_size, num_features)
    gamma, beta: (num_features,)
    Normalize over batch dimension (axis=0)
    """
    mean = X.mean(axis=0, keepdims=True)      # (1, num_features)
    var = X.var(axis=0, keepdims=True)        # (1, num_features)
    X_norm = (X - mean) / np.sqrt(var + eps)
    return gamma * X_norm + beta


def layer_norm(X, gamma, beta, eps=1e-5):
    """
    X: (batch_size, num_features)
    gamma, beta: (num_features,)
    Normalize over feature dimension (axis=1)
    """
    mean = X.mean(axis=1, keepdims=True)      # (batch_size, 1)
    var = X.var(axis=1, keepdims=True)        # (batch_size, 1)
    X_norm = (X - mean) / np.sqrt(var + eps)
    return gamma * X_norm + beta


import torch

def batch_norm(X, gamma, beta, eps=1e-5):
    """
    X: (batch_size, num_features)
    gamma, beta: (num_features,)
    """
    mean = X.mean(dim=0, keepdim=True)
    var = X.var(dim=0, unbiased=False, keepdim=True)
    X_norm = (X - mean) / torch.sqrt(var + eps)
    return gamma * X_norm + beta


def layer_norm(X, gamma, beta, eps=1e-5):
    """
    X: (batch_size, num_features)
    gamma, beta: (num_features,)
    """
    mean = X.mean(dim=1, keepdim=True)
    var = X.var(dim=1, unbiased=False, keepdim=True)
    X_norm = (X - mean) / torch.sqrt(var + eps)
    return gamma * X_norm + beta