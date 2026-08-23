# 只用 NumPy 从零实现 Logistic Regression，不能调用 sklearn。
# 需要完成权重初始化、sigmoid、predict_proba、binary cross-entropy、梯度下降训练和 predict

# 核心公式：
# z = Xw + b
# p = sigmoid(z)
# loss = -mean(ylog(p) + (1-y)log(1-p))
# dw = X.T@(p-y)/n
# db = mean(p-y)

# 面试官会重点看矩阵 shape、梯度来源、向量化实现、时间复杂度和数值稳定性。

# Follow-up
# sigmoid 如何避免 overflow？如何避免 log(0)？为什么 BCE 适合二分类？类别不平衡怎么办?
# 如何加入 L2？如何改成 mini-batch SGD?
# 训练 loss 下降但 validation loss 上升说明什么？