# Task: Implement multi_head_self_attention(X, W_q, W_k, W_v, W_o, num_heads)
# Input:

# X: Input tensor of shape (batch_size, seq_len, d_model)
# W_q, W_k, W_v: Weight matrices, each of shape (d_model, d_model)
# W_o: Output projection of shape (d_model, d_model)
# num_heads: Number of attention heads (assume d_model % num_heads == 0)

# Output: Tensor of shape (batch_size, seq_len, d_model)

# Requirements:

# Compute Q, K, V projections
# Split into num_heads heads (each head has dimension d_k = d_model // num_heads)
# Compute scaled dot-product attention: softmax(QK^T / sqrt(d_k)) * V
# Masked attention (on QK product): Apply a causal mask so position i can only attend to positions ≤ i.
# Concatenate heads and apply output projection


#### 1. Numpy solution
import numpy as np

def multi_head_masked_self_attention(X, W_q, W_k, W_v, W_o, num_heads):
    """
    X: (batch_size, seq_len, d_model)
    W_q, W_k, W_v: (d_model, d_model)
    W_o: (d_model, d_model)
    """
    batch_size, seq_len, d_model = X.shape
    d_k = d_model // num_heads

    # linear projections
    Q = X @ W_q # (batch_size, seq_len, d_model)
    K = X @ W_k
    V = X @ W_v

    # Split to multiple heads (batch_size, num_heads, seq_len, d_k)
    Q = Q.reshape(batch_size, seq_len, num_heads, d_k).transpose(0, 2, 1, 3)
    K = K.reshape(batch_size, seq_len, num_heads, d_k).transpose(0, 2, 1, 3)
    V = V.reshape(batch_size, seq_len, num_heads, d_k).transpose(0, 2, 1, 3)

    # Compute scaled dot-product attention scores softmax(QK^T / sqrt(d_k)) * V
    # (batch_size, num_heads, seq_len, seq_len)
    scores = Q @ K.transpose(0, 1, 3, 2) / np.sqrt(d_k)

    # Mask attention
    mask = np.triu((np.ones(seq_len, seq_len)), k = 1).astype(bool)
    scores = np.where(mask, -np.inf, scores)

    # Softmax
    # For each query position, we want a probability distribution over all keys
    # scores[batch, head, query, :] → softmax → attention weights that sum to 1
    max_score = scores.max(axis = -1, keepdims=True)
    exp_scores = np.exp(scores - max_score)
    attn_weights = exp_scores / exp_scores.sum(axis = -1, keepdims = True)
    attn_outputs = attn_weights @ V # (batch, heads, seq, d_k)
    # attn_weights: (batch, heads, seq_len, seq_len)
    #                               ↑query   ↑key
    # V:            (batch, heads, seq_len, d_k)
    #                               ↑key     ↑value_dim
    # Matrix multiply on last two dimensions:
    # (query, key) @ (key, d_k) → (query, d_k)


    # Concatenate the heads
    attn_outputs = attn_outputs.reshape(0, 2, 1, 3).reshape(batch_size, seq_len, d_model)

    # Output projection
    outputs = attn_outputs @ W_o # (batch_size, seq_len, d_model)
    return outputs




### 2. PyTorch solution
import torch
import torch.nn.functional as F


def multi_head_masked_self_attention(X, W_q, W_k, W_v, W_o, num_heads):
    """
    X: (batch_size, seq_len, d_model)
    W_q, W_k, W_v: (d_model, d_model)
    W_o: (d_model, d_model)
    """
    batch_size, seq_len, d_model = X.shape
    d_k = d_model // num_heads

    # linear projections
    Q = X @ W_q # (batch_size, seq_len, d_model)
    K = X @ W_k
    V = X @ W_v

    # Split to multiple heads (batch_size, num_heads, seq_len, d_k)
    Q = Q.view(batch_size, seq_len, num_heads, d_k).transpose(1, 2) # pytorch transpose only specifiy the two axes to swap
    K = K.view(batch_size, seq_len, num_heads, d_k).transpose(1, 2)
    V = V.view(batch_size, seq_len, num_heads, d_k).transpose(1, 2)

    # Compute scaled dot-product attention scores softmax(QK^T / sqrt(d_k)) * V
    # (batch_size, num_heads, seq_len, seq_len)
    scores = Q @ K.transpose(2, 3) / (d_k ** 0.5)

    # Mask attention
    mask = torch.triu((torch.ones(seq_len, seq_len)), diagonal = 1).astype(bool)
    scores.masked_fill(mask, float('-inf'))

    # Softmax
    # For each query position, we want a probability distribution over all keys
    # scores[batch, head, query, :] → softmax → attention weights that sum to 1
    attn_weights = F.softmax(scores, dim = -1)
    attn_outputs = attn_weights @ V # (batch, heads, seq, d_k)
    # attn_weights: (batch, heads, seq_len, seq_len)
    #                               ↑query   ↑key
    # V:            (batch, heads, seq_len, d_k)
    #                               ↑key     ↑value_dim
    # Matrix multiply on last two dimensions:
    # (query, key) @ (key, d_k) → (query, d_k)


    # Concatenate the heads
    attn_outputs = attn_outputs.transpose(1, 2).contiguous().view(batch_size, seq_len, d_model)

    # Output projection
    outputs = attn_outputs @ W_o # (batch_size, seq_len, d_model)
    return outputs
















