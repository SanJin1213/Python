import numpy as np


# [[0 0 0 0]
#  [0 0 0 0]
#  [0 0 0 0]]
# a = np.zeros((3, 4), dtype=np.int)

# [[1 1 1 1]
#  [1 1 1 1]
#  [1 1 1 1]]
# a = np.ones((3,4), dtype=np.int)

# [ 1  3  5  7  9 11 13 15 17 19]
# a = np.arange(1, 20, 2)

# 设置几行几列 ，可以同时一起使用
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
# a = np.arange(12).reshape((3, 4))

# 设置生成，几段
# [ 0.  5. 10. 15. 20.]
a = np.linspace(0, 20, 5)
print(a)
