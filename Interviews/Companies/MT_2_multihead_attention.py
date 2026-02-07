# Q, K, V: (batch_size, num_heads, seq_len, d_head)
# d_model = num_heads * d_head
# K.transpose: (batch_size, num_heads, d_head, seq_len)
# attention_scores = Q @ K_T / sqrt(d_head) -> (batch_size, num_heads, seq_len, seq_len)
# attention_weights = softmax(attention_scores)
# output = attention_weights @ V # (batch_size, num_heads, seq_len, d_head)

import numpy as np

def softmax(scores): # (batch_size, num_heads, seq_len, seq_len)
    # exp(xi) / sum over j of exp(xj)
    exp_scores = np.exp(scores) 
    return exp_scores / exp_scores.sum(axis = -1, keepdim = True) # (batch_size, seq_len, 1) then broadcasted



def self_attention(X, W_Q, W_K, W_V, W_O, num_heads):
    """  
    :param X: (batch_size, seq_len, d_model)
    :param W_Q, W_K, W_V, W_O: (d_head, d_model)
    """
    batch_size, seq_len, d_model = X.shape
    d_head = d_model // num_heads

    Q = X @ W_Q # (batch_size, seq_len, d_model)
    K = X @ W_K # (batch_size, seq_len, d_model)
    V = X @ W_V # (batch_size, seq_len, d_model)

    Q = Q.reshape(batch_size, seq_len, num_heads, d_head).transpose(0, 2, 1, 3)
    K = K.reshape(batch_size, seq_len, num_heads, d_head).transpose(0, 2, 1, 3)
    V = V.reshape(batch_size, seq_len, num_heads, d_head).transpose(0, 2, 1, 3)

    attn_scores = Q @ K.transpose(0, 1, 3, 2) / np.sqrt(d_head) # (batch_size, num_heads, seq_len, seq_len)
    mask = np.triu(np.ones((seq_len, seq_len), k = 1)).astype(bool) # k = 1 means including diagonal (so can attend to itself)
    masked_attn_scores = np.where(mask, -np.inf, attn_scores)

    attn_weights = softmax(masked_attn_scores)
    attn_output = attn_weights @ V # (batch_size, num_heads, seq_len, d_head)

    # Concatenate the heads
    attn_output = attn_output.transpose(0, 2, 1, 3).reshape(batch_size, seq_len, d_model)

    # Output projection
    output = attn_output @ W_O

    return output


# def self_attention(Q, K, V):
#     batch_size, num_heads, seq_len, d_head = K.shape

#     attention_scores = Q @ K.transpose(0, 1, 3, 2) / np.sqrt(d_head) # (batch_size, num_heads, seq_len, seq_len)
#     mask = np.triu(np.ones((seq_len, seq_len), k = 1)).astype(bool) # k = 1 means including diagonal (so can attend to itself)
#     masked_attention_scores = np.where(mask, -np.inf, attention_scores)

#     attention_weights = softmax(masked_attention_scores)
#     output = attention_weights @ V # (batch_size, num_heads, seq_len, d_head)

#     return output
