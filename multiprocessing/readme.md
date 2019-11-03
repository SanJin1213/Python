# Multiprocessing(多进程学习，多核运算）

## 一、创建并添加process

并添加了比较

```python
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
```

和添加多线程，如出一辙
[详细代码](code/add_multiprocessing.py)

## 二、queue 队列（基本和threading一样)

总结：
一定要先定义一个Queue 并添加到 def 定义的输入值中，**.put**是将进程产生的返回值全部拾取，并保存，**.get** 是将队列中的值一个一个的取出，最后将返回值，进行运算
[详细代码](code/queue_multiprocessing.py)

## 三、 多线程，多进程，和普通的函数，进行效率比较

我的电脑输出结果
normal: 499999666667166666000000
normal time: 2.311807870864868
multithread: 499999666667166666000000
multithread time: 2.264944076538086
multicore: 499999666667166666000000
multicore time: 1.402259349822998

多进程>普通>多线程
[详细代码](code/efficiency_comparison.py)

## 四、 进程池 pool

概念：python将所有的任务放到进程池中，pool 会自己将这些任务怎么分配进程，怎么输出分配等等

#### process 和 pool的区别

process 没有返回值，只能加入queue中然后在用get 取
pool 是有返回值的，可以直接输出

#### 在pool()中，可以指定用核的数量，procesess=

#### map的作用

map  是将def的函数方程和输入值 合并在一起。(莫烦大佬：说是放入函数和需要迭代运算的值)
然后自动分配给cpu核，并返回结果
除了map功能，还有applay_async() 获取pool 的返回结果，参数设置同map，但是要写数字的话，注意迭代，要写成pool.apply_async(job, (2,))
**但是apply_async与map不同**
apply_async 是只能在一个进程中算一个东西，并输出一个返回值，如果想多输出，就要进行输入输出的迭代
输出的时候还要注意，与map 一样是需要获取的，要写成print(res.get())**但是get只能获取一个值**否则报错
![报错](images/1.png)

如果想输出很多，需要使用迭代，遍历列表 输入输出都要使用

```python
multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
print([res.get() for res in multi_res])
```

[具体代码](code/pool_multiprocessing.py)

## 五、共享内存

为什么会使共享内存？
因为只有这样，才能让CPU之间有交流
用.Value() 里面需要有两个参数，一个是你要共享数据的数据类型，另一个是内容在多核之间共享
[更多数据类型](https://docs.python.org/3.5/library/array.html)

```python
import multiprocessing as mp


# 定义它，需要给它一个类型
# i 是整数 d 是小数
value1 = mp.Value("i", 0)
value2 = mp.Value("d", 3.14)
```

还有一个共享的类是Array 这是一个一维数组，也是要定义数据类型，都这会报错
同样可以在上面的**更多数据类型**，查看具体内容
抓取共享内存，用 变量名.value (小写)

## 六、 进程锁lock

没有锁就会出现一种强进程的现象，看谁抢到了，就输出谁
普通代码

```python
import multiprocessing as mp
import time


def job(v, num):
    for _ in range(5):
        time.sleep(0.1)
        v.value += num
        print(v.value)


def multicore():
    v = mp.Value('i', 0)
    p1 = mp.Process(target=job, args=(v, 1))
    p2 = mp.Process(target=job, args=(v, 3))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    multicore()
```

定义进程锁  l = mp.Lock()
加入到函数的输入值  def job(v, num, l):
上锁   l.acquire()
解锁   l.release()
[具体代码](code/lock_multiprocessing.py)