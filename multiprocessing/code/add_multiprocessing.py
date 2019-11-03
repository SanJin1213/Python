import multiprocessing as mp
# import threading as td


def job(a, b):
    print("aaaaaaa")


# multiprocessing 运用一定要加if。。。。（固定格式）
if __name__ == "__main__":
    # # args 代表 进程中的参数名
    # t1 = td.Thread(target=job, args=(1, 2))
    # 类似指定多核中的一个核，不确定这样的说法
    p1 = mp.Process(target=job, args=(1, 2))

    # t1.start()
    p1.start()
    # t1.join()
    p1.join()
