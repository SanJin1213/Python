import multiprocessing as mp


def job(q):
    res = 0
    for i in range(1000):
        res += i + i**2 + i**3
    # 将结果放入queue
    q.put(res)


if __name__ == "__main__":
    q = mp.Queue()
    # 为了防止报错，在q的后面加上，
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # 再重新获取队列中的值，进行加载
    res1 = q.get()
    res2 = q.get()
    print(res1 + res2)
