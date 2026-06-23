### Numpy solution

import numpy as np

def batch_norm(X, gamma, beta, eps=1e-5):
    """
    Batch Normalization
    
    Input:
        X: (batch_size, num_features) - e.g., (32, 512)
        gamma: (num_features,) - learnable scale
        beta: (num_features,) - learnable shift
    
    What it does:
        For EACH FEATURE, compute mean and variance ACROSS ALL SAMPLES in the batch.
        Then normalize so each feature has mean=0, variance=1 across the batch.
    
    Normalize over: axis=0 (batch dimension)

    Formula:
    X_norm = (X - mean)/sqrt(var + eps)
    X_output = X_norm * gamma + beta
    
    Example with X of shape (4 samples, 3 features):
    
        Feature→   f1    f2    f3
        Sample 0 [[1.0,  2.0,  3.0],
        Sample 1  [1.5,  2.5,  3.5],
        Sample 2  [1.2,  2.2,  3.2],
        Sample 3  [1.3,  2.3,  3.3]]
                   ↓     ↓     ↓
                  mean  mean  mean   ← normalise each column
    
    Use case: CNNs, fixed batch sizes
    Problem: Depends on other samples — different behavior at train vs inference
    """
    mean = X.mean(axis = 0, keepdims = True) # (1, num_features)
    var = X.var(axis = 0, keepdims = True) # (1, num_features)
    X_norm = (X - mean) / np.sqrt(var + eps)
    X_output = X_norm * gamma + beta # element-wise multiplication, not matrix multiplication @

    return X_output

    


def layer_norm(X, gamma, beta, eps=1e-5):
    """
    Layer Normalization
    
    Input:
        X: (batch_size, num_features) - e.g., (32, 512)
        gamma: (num_features,) - learnable scale
        beta: (num_features,) - learnable shift
    
    What it does:
        For EACH SAMPLE, compute mean and variance ACROSS ALL FEATURES.
        Then normalize so each sample has mean=0, variance=1 across its features.
    
    Normalize over: axis=1 (feature dimension)
    
    Example with X of shape (4 samples, 3 features):
    
        Feature→   f1    f2    f3
        Sample 0 [[1.0,  2.0,  3.0],  → mean, var → normalize this row
        Sample 1  [1.5,  2.5,  3.5],  → mean, var → normalize this row
        Sample 2  [1.2,  2.2,  3.2],  → mean, var → normalize this row
        Sample 3  [1.3,  2.3,  3.3]]  → mean, var → normalize this row
    
    Use case: Transformers, RNNs, variable batch sizes
    Advantage: Each sample normalized independently — same behavior train & inference
    """
    mean = X.mean(axis = 1, keepdims = True) # (batch_size, 1)
    var = X.var(axis = 1, keepdims = True) # (batch_size, 1)
    X_norm = (X - mean) / np.sqrt(var + eps)
    X_output = X_norm * gamma + beta # element-wise multiplication, not matrix multiplication @

    return X_output




### PyTorch solution

import torch

def batch_norm(X, gamma, beta, eps=1e-5):
    """
    Batch Normalization
    
    Input:
        X: (batch_size, num_features) - e.g., (32, 512)
        gamma: (num_features,) - learnable scale
        beta: (num_features,) - learnable shift
    
    What it does:
        For EACH FEATURE, compute mean and variance ACROSS ALL SAMPLES in the batch.
        Then normalize so each feature has mean=0, variance=1 across the batch.
    
    Normalize over: axis=0 (batch dimension)

    Formula:
    X_norm = (X - mean)/sqrt(var + eps)
    X_output = X_norm * gamma + beta
    
    Example with X of shape (4 samples, 3 features):
    
        Feature→   f1    f2    f3
        Sample 0 [[1.0,  2.0,  3.0],
        Sample 1  [1.5,  2.5,  3.5],
        Sample 2  [1.2,  2.2,  3.2],
        Sample 3  [1.3,  2.3,  3.3]]
                   ↓     ↓     ↓
                  mean  mean  mean   ← normalise each column
    
    Use case: CNNs, fixed batch sizes
    Problem: Depends on other samples — different behavior at train vs inference
    """
    mean = X.mean(dim = 0, keepdims = True) # (1, num_features)
    var = X.var(dim = 0, keepdims = True) # (1, num_features)
    X_norm = (X - mean) / torch.sqrt(var + eps)
    X_output = X_norm * gamma + beta # element-wise multiplication, not matrix multiplication @

    return X_output

    


def layer_norm(X, gamma, beta, eps=1e-5):
    """
    Layer Normalization
    
    Input:
        X: (batch_size, num_features) - e.g., (32, 512)
        gamma: (num_features,) - learnable scale
        beta: (num_features,) - learnable shift
    
    What it does:
        For EACH SAMPLE, compute mean and variance ACROSS ALL FEATURES.
        Then normalize so each sample has mean=0, variance=1 across its features.
    
    Normalize over: axis=1 (feature dimension)
    
    Example with X of shape (4 samples, 3 features):
    
        Feature→   f1    f2    f3
        Sample 0 [[1.0,  2.0,  3.0],  → mean, var → normalize this row
        Sample 1  [1.5,  2.5,  3.5],  → mean, var → normalize this row
        Sample 2  [1.2,  2.2,  3.2],  → mean, var → normalize this row
        Sample 3  [1.3,  2.3,  3.3]]  → mean, var → normalize this row
    
    Use case: Transformers, RNNs, variable batch sizes
    Advantage: Each sample normalized independently — same behavior train & inference
    """
    mean = X.mean(dim = 1, keepdims = True) # (batch_size, 1)
    var = X.var(dim = 1, keepdims = True) # (batch_size, 1)
    X_norm = (X - mean) / torch.sqrt(var + eps)
    X_output = X_norm * gamma + beta # element-wise multiplication, not matrix multiplication @

    return X_output