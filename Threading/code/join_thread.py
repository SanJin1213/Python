import threading
import time 


def thread_jod():
    print("T1 start \n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish \n")


def T2_job():
    print("T2 start \n")
    print("T2 finish \n")


def main():
    # 创建一个线程
    added_thread = threading.Thread(target=thread_jod, name="T1")
    thread2 = threading.Thread(target=T2_job, name="T2")
    # 进程的开始
    added_thread.start()
    thread2.start()
    # 运行完上面的线程，在执行下面的print
    added_thread.join()
    thread2.join()
    print("all done \n")
  

if __name__ == "__main__":
    main()
