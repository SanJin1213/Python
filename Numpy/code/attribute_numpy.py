import numpy as np


# 将列表转化成数组
array = np.array([[1, 2, 3],
                  [2, 3, 4]])

print(array)
# ndim 代表是几维数组
print("number of dim:", array.ndim)
# shape 代表数组的行数和列数
print("array shape:", array.shape)
# size 是代表元素的个数
print("size:", array.size)
