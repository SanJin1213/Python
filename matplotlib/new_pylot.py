from matplotlib import pyplot as plt

# 设置图片大小和清晰度
fig = plt.figure(figsize=(20, 8), dpi=80)

x = range(2, 26, 2)
y = [15, 20, 25, 14, 25, 31, 21, 43, 23, 12, 12, 13]

# 自动绘图
plt.plot(x, y)
# 设置x轴的刻度
plt.xticks(x)
# 为什么+1 因为，range 不取最后一个数值，是左闭右开这种类型，所以得+1 range（0，9）的意思是从0开始，到8，不包含9，想取最大值，需+1
plt.yticks(range(min(y), max(y)+1))  
# plt.xticks(x[::3])  # 3 代表去取3个原x中的步长，也就是3*4=12 这是两个数之间想个的实际距离
# 保存
# plt.savefig("./plt01.png")
# 显示
plt.show()
