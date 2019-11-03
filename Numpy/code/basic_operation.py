import numpy as np


# a = np.array([10, 20, 30, 40])
# b = np.arange(4)

# 基础运算，加、减、乘、平方(每个元素减每个元素)
# c = a-b
# [10 19 28 37]

# c = a + b
#  [10 21 32 43]

# c = a * b
# [  0  20  60 120]


# c = a**2
# [ 100  400  900 1600]

# sin cos tan 等三角函数运算
# c = np.cos(a)
# [-0.83907153  0.40808206  0.15425145 -0.66693806]

# 对数组使用print函数进行逻辑运算
# print(b)
# print(b < 3)
# [0 1 2 3]
# [ True  True  True False]

# print(c)

# 多维数组进行运算

# a = np.array([[1, 0],
#               [3, 4]])
# b = np.arange(4).reshape((2, 2))

# # 一维数组
# c = a * b
# # [[ 0  0]
# #  [ 6 12]]

# # 多维数组的两种结果相同的运算方法
# c_dot = np.dot(a, b)
# c_dot_1 = a.dot(b)
# # [[ 0  1]
# #  [ 8 15]]

# print(c)
# print(c_dot)
# print(c_dot_1)

# # 引用随机数
# a = np.random.random((2, 4))
# # [[0.20334667 0.84825336 0.60467202 0.48531244]
# #  [0.56401268 0.02925453 0.5699665  0.94572479]]
# b = np.sum(a)
# c = np.min(a)
# d = np.max(a)

# # # 5.172096323139666
# # 0.45204760427530255
# # 0.925723724969528
# print(a)
# print(b)
# print(c)
# print(d)

A = np.arange(2, 14).reshape((3, 4))
# print(A)
# # [[ 2  3  4  5]
# #  [ 6  7  8  9]
# #  [10 11 12 13]]
# print(np.nonzero(A))
# (array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2], dtype=int64), array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3], dtype=int64))
# print(np.transpose(A))
# print(A.T.dot(A)) == A.T
print(np.clip(A, 3, 9))
