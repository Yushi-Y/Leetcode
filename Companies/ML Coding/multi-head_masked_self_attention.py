# Task: Implement multi_head_self_attention(X, W_q, W_k, W_v, W_o, num_heads) with Numpy
# Input:

# X: Input tensor of shape (batch_size, seq_len, d_model)
# W_q, W_k, W_v: Weight matrices, each of shape (d_model, d_model)
# W_o: Output projection of shape (d_model, d_model)
# num_heads: Number of attention heads (assume d_model % num_heads == 0)

# Output: Tensor of shape (batch_size, seq_len, d_model)


### Thoughts
# Project X unto Q,K,V - linear projections
# * Multi-head: reshape and split Q,K,V d_model into d_k
# attention scores: (Q*K^T)/sqr(d_k), d_k = d_model // num_heads 
# mask the attention scores - previous tokens cannot obtain to later tokens 
## In the attention score matrix, rows are queries (the token doing the attending) and columns are keys (the tokens being attended to). 
## Entry (i, j) = how much token i attends to token j. Causal masking forbids attending to the **future**, i.e. entries where j > i — and those live in the upper-right triangle (above the diagonal).
## so matrix upper right triangular part is -inf
# softmax on attention scores
## Why need softmax? The next step is weights @ V — a convex combination of value vectors. For that to be a sensible "blend," each row must be non-negative and sum to 1. Raw dot products can be anything: negative, huge, unbounded. 
## Softmax converts them into a proper probability distribution: "token 1 takes 60% of its information from token 3, 30% from token 0, 10% from itself."
## Attention is conceptually a soft lookup: "which tokens are relevant?" A hard argmax (pick the single best key) would be non-differentiable, so gradients couldn't flow through the selection. Softmax is a smooth approximation of argmax — hence the name soft-max — letting the model learn what to attend to via backprop.
# then multiply with V
# concatenate d_k back to d_model
# multiply W_o to get (B,S,D)

import numpy as np

def softmax(X): 
    # X - can be > 2D dimension
    # exp(x_i) / sum(exp(x_i)) for x_i in X
    # in practice, we normalise by subtracting x_i = x_i - max(x_i) to prevent exp explode: inf/inf or divide by zero
    X_norm = X - np.max(X)
    exp_X = np.exp(X_norm, axis = -1, keepdims = True)
    return exp_X / np.sum(exp_X, axis = -1, keepdims = True)


def multi_head_masked_self_attention(X, W_q, W_k, W_v, W_o, num_heads):
    """
    X: (batch_size, seq_len, d_model)
    W_q, W_k, W_v: (d_model, d_model)
    W_o: (d_model, d_model)
    """
    B, S, D = X.shape
    d_k = D // num_heads

    # Project X unto Q,K,V
    Q = X @ W_q
    K = X @ W_k
    V = X @ W_v

    # split d_model into d_k
    Q = Q.reshape(B, S, d_k, num_heads).transpose(0, 3, 1, 2)
    K = K.reshape(B, S, d_k, num_heads).transpose(0, 3, 1, 2)
    V = V.reshape(B, S, d_k, num_heads).transpose(0, 3, 1, 2)

    # attention scores
    # Q - (B, num_heads, S, d_k)
    # K - (B, num_heads, d_k, S)
    # Attention scores matrix - (B, num_heads, S, S)
    attention_scores = np.matmul(Q, K.transpose(0, 1, 3, 2)) / np.sqrt(d_k)

    # masking
    # lower left triangle (including diagonal) is zero
    # upper right is -inf
    mask = np.triu(np.ones((S, S)) * -1e12)
    attention_scores = attention_scores + mask

    # softmax
    # turn each query token's raw scores over all keys to a set of weights
    attention_weights = softmax(attention_scores)

    # multiple with V
    # (B, num_heads, S, d_k)
    result = np.matmul(attention_weights, V)

    # concatenate heads back
    # (B, S, num_heads, dk) -> (B,S,D)
    concat_result = result.transpose(0, 2, 1, 3).reshape(B,S,D)

    # multiply with W_o
    output = np.matmul(concat_result, W_o) # (B,S,D)

    return output








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
    attn_outputs = attn_outputs.transpose(0, 2, 1, 3).reshape(batch_size, seq_len, d_model)

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
















