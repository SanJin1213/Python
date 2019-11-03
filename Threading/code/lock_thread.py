import threading


def job1():
    global A, lock
    # 设定锁
    lock.acquire()
    for i in range(10):
        A += 1
        print("job1", A)
    # 解锁
    lock.release()


def job2():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 10
        print("job2", A)
    lock.release()


if __name__ == "__main__":
    # 添加锁函数
    lock = threading.Lock()
    # 并将lock 设置为全局变量
    A = 0
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()