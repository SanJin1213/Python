import multiprocessing as mp


# 定义它，需要给它一个类型
# i 是整数 d 是小数
value1 = mp.Value("i", 0)
value2 = mp.Value("d", 3.14)