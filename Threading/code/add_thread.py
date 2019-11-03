import threading


# 制定进程工作的函数
def thread_jod():
    # 输出这是一个添加线程，
    print("This is add thread, number is %s" % threading.current_thread())


def main():
    # 添加线程,并指定进程的工作
    add_thread = threading.Thread(target=thread_jod)
    # # 查看当前启动的线程的个数
    # print(threading.active_count())
    # # 查看具体启动了哪几个线程
    # print(threading.enumerate())
    # # 查看运行程序是哪个线程在运行
    # print(threading.current_thread())
    # 定义进程开始
    add_thread.start()


if __name__ == "__main__":
    main()
