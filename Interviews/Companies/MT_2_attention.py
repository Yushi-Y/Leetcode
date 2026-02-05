# Q, K, V: (batch_size, seq_len, d_model)
# K.transpose: (batch_size, d_model, seq_len)
# attention_scores = Q @ K_T / sqrt(d_model) -> (batch_size, seq_len, seq_len)
# attention_weights = softmax(attention_scores)
# output = attention_weights @ V # (batch_size, seq_len, d_model)

import numpy as np

def softmax(scores): # (batch_size, seq_len, seq_len)
    # exp(xi) / sum over j of exp(xj)
    exp_scores = np.exp(scores) 
    return exp_scores / exp_scores.sum(axis = -1, keepdim = True) # (batch_size, seq_len, 1) then broadcasted
    

def self_attention(Q, K, V):
    batch_size, seq_len, d_model = K.shape

    attention_scores = Q @ K.transpose(0, 2, 1) / np.sqrt(d_model) # (batch_size, seq_len, seq_len)
    mask = np.triu(np.ones((seq_len, seq_len), k = 1)).astype(bool) # k = 1 means excluding diagonal (so not attending to itself)
    masked_attention_scores = np.where(mask, -np.inf, attention_scores)

    attention_weights = softmax(masked_attention_scores)
    output = attention_weights @ V # (batch_size, seq_len, d_model)

    return output
