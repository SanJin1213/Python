import multiprocessing as mp


def job(x):
    return x * x


def multicore():
    # 不加参数，就是默认使用所有的核
    # 要设置用几个核 用processes=
    pool = mp.Pool()
    res = pool.map(job, range(10))
    res1 = pool.apply_async(job, (2,))
    multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
    # res2 = pool.apply_async(job, range(10))
    print(res)
    print(res1) 
    # 输出结果 <multiprocessing.pool.ApplyResult object at 0x000002702D525F28>
    print(res1.get())
    # 只能获取一个值
    # print(res2.get())
    # 输出也要进行迭代
    print([res.get() for res in multi_res])


if __name__ == "__main__":
    multicore()
# 输出结果 [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
