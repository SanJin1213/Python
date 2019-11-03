# Threading 学会多线程

## 一、添加线程

```python
    # 添加线程，target 是指定线程的工作，可以是一个函数
    threading.Thread(target=thread_jod，name=)
    # 开始
    进程名.start()

```

[具体代码](code/add_thread.py)

## 二、 join功能

“等待该线程终止。”

解释一下，是主线程等待子线程的终止。也就是说主线程的代码块中，如果碰到了t.join()方法，此时主线程需要等待（阻塞），等待子线程结束了(Waits for this thread to die.),才能继续执行t.join()之后的代码块。
[具体代码](code/join_thread.py)

## 三、Queue 功能

多线程是没有返回值的，我们把线程预算出来的结果放在一个长的队列中，每一个线程的队列到主线程以后再拿出来，再继续进行操作。

[具体代码](code/Queue_thread.py)

## 四、GIL(全局解析锁)

 Python 的设计上, 有一个必要的环节, 就是 **Global Interpreter Lock (GIL)**,这个东西让 Python 还是**一次性只能处理一个东西**。尽管Python完全支持多线程编程， 但是解释器的C语言实现部分在完全并行执行时并不是线程安全的。 实际上，**解释器被一个全局解释器锁保护着，它确保任何时候都只有一个Python线程执行。GIL最大的问题就是Python的多线程程序并不能利用多核CPU的优势** （比如一个使用了多个线程的计算密集型程序只会在一个单CPU上面运行）。
在讨论普通的GIL之前，<font color=#ff000>有一点要强调的是GIL只会影响到那些严重依赖CPU的程序（比如计算型的）。 如果你的程序大部分只会涉及到I/O，比如网络交互，那么使用多线程就很合适， 因为它们大部分时间都在等待。</font>实际上，你完全可以放心的创建几千个Python线程， 现代操作系统运行这么多线程没有任何压力，没啥可担心的。

什么是GIL(Global Interpreter Lock)
Python作为一门编程语言，可没有定义GIL, 这玩意其实是Python解析器CPython用来做多线程控制和调度的全局锁，Python还有一些别的解析器，比如JPython, Pypy等，其中JPython就没有GIL。但是CPython现在已经成为Python的实际标准，各种Linux和其它OS默认集成的Python, 以及从官方网站上下载的Python，还有各种相关的工具如pip等都在使用CPython，所以GIL问题自然也就成为了Python语言的 问题了。
GIL的问题其实是由于近十几年来应用程序和操作系统逐步从多任务单核心演进到多任务多核心导致的 , 在一个古老的单核CPU上调度多个线程任务，大家相互共享一个全局锁，谁在CPU执行，谁就占有这把锁，直到因为IO或者Timer Tick到期让出CPU，没有在执行的线程就安静的等待着这把锁（除了等待之外，他们应该也无事可做）：
![单核cpu](images/1.jpeg)
单核CPU上线程调度
很明显，在一个现代多核心的处理器上，上面的模型就有很大优化空间了，原来只能等待的线程任务，现在可以在其它空闲的核心上调度并发执行。由于古老GIL机制，如果线程2需要在CPU 2上执行，它需要先等待在CPU 1上执行的线程1释放GIL，要命的是，在Python 2.x, 线程A不会动态的调整自身的优先级，所以很大概率下次被选中执行的还是A，在很多个这样的选举周期内，线程2只能安静的看着线程1拿着GIL在CPU 1上欢快的执行。
![单核cpu](images/2.jpeg)
多核CPU上线程2由于等待线程1释放GIL而不能执行
在稍微极端一点的情况下，比如线程1使用了while 1在CPU 1 上执行，那就真是“一核有难，八核围观”了。
![单核cpu](images/3.jpeg)
一核有难，八核围观


### 五、 使用Lock
首先添加Lock到程序中
分别给要添加到线程的函数设置锁
还需要将lock 添加到全局变量
    # 设定锁
    lock.acquire()
      # 解锁
    lock.release()

[具体代码](code/lock_thread.py)