import numpy as np


A = np.arange(1, 8)
# print(A[2])
# # 3
B = np.arange(2, 14).reshape((3, 4))
# print(B[2])
# # 输出了第二行的所有元素
# # [10 11 12 13]
# print(B[2, 3])  # 13
# print(B[2][3])  # 13

# # 逐列遍历矩阵
# for row in B:
#     print(row)
# # [2 3 4 5]
# # [6 7 8 9]
# # [10 11 12 13]

# # 逐行输出矩阵
# for column in B.T:
#     print(column)
# """
#     输出结果
#    [ 2  6 10]
#     [ 3  7 11]
#     [ 4  8 12]
#     [ 5  9 13]
# """

# # 一共三行，所以看成三个元素，遍历了三遍
# for i in B:
#     print(B)

print(B.flatten())

for item in A.flat:
    print(item)