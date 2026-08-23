# RoPE 位置编码 - numpy

# rotary position embedding
# 通过旋转矩阵将位置信息编码到 Query 和 Key 中的方法。
### 核心思想：
# 对于位置 m 的向量，将其每两个维度视为一个复数，乘以旋转因子 e^imθ_k：
# f(q, m) = q · e^imθ
# 其中旋转角度定义为：
# θ_k = 1/(10000^2k/d), k = 0, 1, …, d/2-1
# base = 10000 是个超参，控制旋转频率/速度的
# 两个位置 m, n 的内积只依赖于相对位置 $m - n$

# 关键性质 - 相对位置不变性： <f(q, m), f(k, n)> = g(q, k, m-n)
### 实际运算
# θ_k = 1/(10000^2k/d), k = 0, 1, …, d/2-1
# x′=xcos(mθi​)−ysin(mθi​)
# y′=xsin⁡(mθi)+ycos⁡(mθi)y'
# 设 head_dim 为 d，向量 x
# RoPE(x,m)=x⊙cos⁡(mθ)+rotate_half(x)⊙sin⁡(mθ)


import numpy as np
import torch
import math
import torch.nn as nn

def get_rope_angle(dim, base):
    """Compute the theta angle"""
    # k = [0, 1, …, d/2-1]
    k = np.arange(0, dim / 2)
    theta = 1 / (base ** (2 * k / dim))
    return theta

    
def get_rope_cos_sin(dim, base, seq_len):
    """计算cos和sin value at every token position"""
    theta = get_rope_angle(dim, base)
    
    m = np.arange(0, seq_len) # (seq_len)

    # Step 2: 每个位置 m 乘每个转速 theta_i -> 角度表 m * theta_i
    m_theta = np.outer(m, theta)  # (seq_len, d/2)

    # Step 3: 取 cos / sin，并复制一份对齐到完整维度 d
    m_theta = np.concatenate([m_theta, m_theta])

    cos = np.cos(m_theta) # (seq_len, d)
    sin = np.cos(m_theta) # (seq_len, d)

    return cos, sin


def rotate_half(x):
    """旋转操作, rotate_half:(x,y)↦(−y,x)
    将向量后半部分取负并与前半部分交换
    rotate_half([x1, x2, ..., x_{d/2}, x_{d/2+1}, ..., x_d])
             = [-x_{d/2+1}, ..., -x_d, x1, ..., x_{d/2}]
    Args:
        x: shape (..., dim)
    Returns:
        rotated x: shape (..., dim)
    """
    half = x.shape[-1] // 2 
    x1 = x[..., :half]
    x2 = x[..., half:]
    return np.concatenate([-x2, x1])


def rope_apply(x, cos, sin):
    """应用rope
    x⊙cos⁡(mθ)+rotate_half(x)⊙sin⁡(mθ)"""
    return x * cos + rotate_half(x) * sin




##### Complete RoPE attention #####
def rotate_half(x):
    # Split the last dimension in half and rotate
    x1, x2 = x[..., :x.shape[-1] // 2], x[..., x.shape[-1] // 2:]
    return torch.cat((-x2, x1), dim=-1)

def apply_rotary_pos_emb(q, k, cos, sin):
    # Apply the rotary transformation
    q_embed = (q * cos) + (rotate_half(q) * sin)
    k_embed = (k * cos) + (rotate_half(k) * sin)
    return q_embed, k_embed


class RoPEAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.d_model = d_model
        self.head_dim = d_model // num_heads
        
        self.q_proj = nn.Linear(d_model, d_model)
        self.k_proj = nn.Linear(d_model, d_model)
        self.v_proj = nn.Linear(d_model, d_model)
        self.out_proj = nn.Linear(d_model, d_model)
        
    def forward(self, x, cos, sin):
        batch_size, seq_len, _ = x.shape
        
        # 1. Project to Q, K, V and reshape for multi-head attention
        q = self.q_proj(x).view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        k = self.k_proj(x).view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        v = self.v_proj(x).view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        
        # 2. Inject positional information using RoPE
        # Ensure cos and sin are properly broadcastable to [batch, num_heads, seq_len, head_dim]
        q, k = apply_rotary_pos_emb(q, k, cos, sin)
        
        # 3. Standard scaled dot-product attention
        scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.head_dim)
        attn_weights = torch.softmax(scores, dim=-1)
        
        out = torch.matmul(attn_weights, v)
        
        # 4. Reshape back to [batch, seq_len, d_model] and project
        out = out.transpose(1, 2).contiguous().view(batch_size, seq_len, self.d_model)
        return self.out_proj(out)