import threading
from queue import Queue


def job(l, q):
    for i in range(len(l)):
        l[i] = l[i]**2
    # 将l放到q里面
    q.put(l)


def multithreading():
    q = Queue()
    threads = []
    data = [[1, 2, 3], [3, 4, 5], [4, 4, 4], [5, 5, 5]]
    # 将data 中的数据分批次放入线程中，每一个线程运算一批数据，
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q))
        # 线程开始
        t.start()
        # 蒋线程加载到列表
        threads.append(t)
    for thread in threads:
        thread.join()
    result = []
    # 等到线程全部运行完了之后
    # 再一次一次的获取q的值拿出来，放到q
    for k in range(4):
        # .get() 按顺序从q里拿出一个，只能拿出一个
        result.append(q.get())
    print(result)


if __name__ == "__main__":
    multithreading()
