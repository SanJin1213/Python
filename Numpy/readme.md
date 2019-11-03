# Numpy 学习

## 一、 numpy的简单属性

+ **.ndim**    查询是几维矩阵
+ **.shape**   查询矩阵是几行几列
+ **.size**    查询元素的个数
[具体代码](code/attribute_numpy.py)

## 二、 numpy的创建

1. 创建矩阵
    np.array()

2. dtype 是矩阵中元素的数据类型

    + dtype=np.int 整型 默认int是64 如果是32 将改为int32
    + dtype=np.float 小数型 同样默认是64 位数越小所占空间越小，精确是64最精确

3. 生成全部为数字的几行几列的矩阵

    ```python
            np.zeros((3,4), dtype=np.int)
    ```

4. 定义有序的矩阵

    ```python
            np.arange(开头，结尾，步长)
    ```

5. 重新定义行数和列数

    ```python
            np.arange(12).reshape((3,4))
    ```

6. 生成几段

    ```python
            np.linspace(开始，结束，多少段)
    ```

[具体代码](code/set_up_numpy.py)

## 三、 numpy 的基本运算

1. 一维矩阵的运算
    1. 加减乘，平方，和普通运算一样，每列的互相做运算
    2. sin cos tan 等三角函数运算
2. 多维矩阵的运算
    1. 乘法
    np.dot(a, b)
    a.dot(b)
    以上两种形式都可以实现多维矩阵的乘法
3. 引用随机数
    np.random.random((行数， 列数)
4. sum min max
    np.sum() (其他相同)
    np.sum(a,axis=0) 在a中 每列操作 axis=1 是每行操作
5. 取最大值、最小值的索引
    np.argmin()
    np.argmax()
6. 求平均数(三种)
    np.mean()
    np.average()
    A.mean()
    A.average
    A.median()  中位数
7. cumsum()函数
    概念：多维矩阵中，开始向，一直加到最后一项输出
    例如： A=矩阵[2,3,4,5]
    np.cumsum(A) [2,2+3=5,2+3+4=9,2+3+4+5=14] [2,5,9,14]
    np.cumsum()
8. 累差元素函数 np.diff()
    概念：后一项减前一项的差
    以上面矩阵为例
    np.diff(A) [1,1,1]
9. 所有非零元素的行和列分开函数 np.nonzero()
    输出结果：(array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2], dtype=int64), array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3], dtype=int64))
    前一个array代表的是非零数字的行坐标，第二代表非零数字的列坐标，从0开始
10. 排序 np.sort() 仅对每一行的元素进行排序
    默认降序排列
11. 矩阵的反向，例如开始是一个3行4列的，通过函数变成4行3列的
    np.transpose()
12. 比较，即跟当前的最大值，最小值比较，如果有比最大值大的数和比最小值小的数都会变成你输入的最大值，最小值，**如果在最大值最小值之间的数，将不受影响**
    np.clip(矩阵名，最小值，最大值)
        [3 3 4 5]
        [6 7 8 9]
        [9 9 9 9]
13. 以上的方法函数，基本都可以添加**axis的属性**
[具体代码](code/basic_operation.py)

## 四、 numpy的索引

1. 一维矩形索引，针对于一维矩阵
    A[2] 代表一维矩阵中第三个元素
    如果是多维矩阵，A[2] 则代A矩阵中的第三行矩阵的所有元素输出
2. 二维矩阵的索引
    A[2][3] 代表二维矩阵中，第三行第四列的元素
    A[2,3] 同上
    也可以指定多个元素
    A[2,1:3] 代表第三行，从第二到第三列的所有元素，不包含第四列的元素
3. 循环遍历矩阵
    逐行：
        for row in A:
    逐列：
        先将矩阵反向，排列，在遍历
        for column in A.T:
4. 迭代输出
    .flatten() 是一个展开性质的函数，将多维的矩阵进行展开成一行的数列
    输出结果：
    [ 2  3  4  5  6  7  8  9 10 11 12 13]
    .flat 是一个迭代器，本身是一个object的属性,像是都展成一列的
    输出结果：
    1
    2
    3
    4
    5
    6
    7

## 五、numpy 的合并

1. 上下合并 v代表竖，类似列
    np.vstack()
    本身是一种上下合并，即对括号中的两个整体进行对应操作
2. 左右合并 h代表横，类似行
    np.hstack()
    是一种左右合并，
3. .shape 是输出行数和列数的方法，如果没有行数或者列数，就只输出一个
4. 对行或列增加维度
    np.newaxis()
    一维矩阵增加维度：
                    行：就是相当于以行的形式输出矩阵
                    列：就是相当于以列的形式输出矩阵
    多维矩阵增加维度：
    : , np.newaxis() 是在第一行矩阵前加一个维度，输出(1,3,3)
    np.nwxaxis(), : 是在第一列矩阵后 加一个维度，输出(3,1,3)
5. 多个矩阵或者数列进行合并
    合并行
    np.concatenate((多个矩阵名字), axis=0)
    合并列
    np.concatenate((多个矩阵的名字), asix=1)
优点，比横向竖向更方便，操作步骤变少

## 六、 numpy 的分割

1. 纵向分割和竖向分割
    np.split(A, 2, axis=0) 参数意思：
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;A 矩阵的名字
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;2 分割成几个元素为一个矩阵
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;axis= 0 代表从行开始分割(横向分割)
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;1 代表从列开始分割(竖向分割)
2. split 是一个等量的分割
3. 解决以上问题：不等量分割
    &emsp; np.array_split()
4. 其他分割方式 vsplit hsplit
&emsp;vsplit 相当于1中的axis=0
&emsp;hsplit 相当于1中的axis=1

## 七、numpy 的”浅拷贝“和”深拷贝“

1. = 就相当于浅拷贝，更改同一地址的数据，每个引用这个地址的对象都会随之改变
2. .copy() 相当于深拷贝，只改变要修改的，不改变其他关联项的数值