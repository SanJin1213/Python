import numpy as np


X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# 输出 (1,3,3)
print(X[np.newaxis, :].shape)
# (3,3)
print(X.shape)
# (3, 1, 3)
print(X[:, np.newaxis].shape)

