from matplotlib import pyplot as plt
import random
# 中文输出文字的办法
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\simfang.ttf")
x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]
plt.figure(figsize=(20, 8), dpi=80)

plt.plot(x, y)
# 强改类型之后，用（）然后在在后面加类型的条件
# _x = list(x)[::3]
_xticks_labels = ["10点{}分".format(i) for i in range(60)]
# 也可以写成_xticks_labels = ["11点{}分".format(i) for i in range(60)
_xticks_labels += ["11点{}分".format(i-60) for i in range(60, 120)]  

# 简化代码 去补偿，数字和字符串一一对应，数据的长度一样
plt.xticks(list(x)[::3], _xticks_labels[::3], rotation=45, 
           fontproperties=my_font)
# rotation代表旋转角度，中文还是这里还是在定义一下
plt.show()
