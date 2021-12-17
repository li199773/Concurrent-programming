# `Concurrent-programming-python` 并发编程
# 总结：线程，进程，协程      
## 1.进程，线程的创建：
### 方式一：直接进行创建：
        from multiprocessing import Process
        t = threading.Thread(target=, args=(,)) # target=传递函数,arg传递变量，是一个元祖，一个元素的话要加逗号
        p = Process(target=func, args=(123,)) 
        p.start()
        t.start()
### 方式二：使用类进行创建：
        class My_Thread(threading.Thread): # 继承父类进行改写
            def __init__(self, filename):  # 定义初始化的方法
                # 必要进行还要处理父类
                super().__init__()
                self.filename = filename
## 2.共享全局变量问题：
### 1.想在函数里面修改使用和修改全局变量的问题使用`global`函数，修改之后输出的值发生改变
### 2.或者使用一个值进行接收，然后对这个值进行修改，初始值并不会被修改
        global a
        b = a  # 或者传一个值进行接收
## 3.生产者和消费者模式：
### 相关说明：
#### 1.3个对象，生产者进行生产，中间者，消费者进行消费，生产者和消费者同时进行
#### 2.定义锁：
        lock = threading.Lock()
        lock.acquire() # 上锁
        lock.release() # 解锁
## 4.队列：先进先出模式。
        q = Queue # 创建队列
        q.put(1) # 队列元素的插入
        print(q.get()) # 队列元素的取出
#### --------------------------------------------------------------------------------------------------------------
# project 项目练习
## 具体练习说明查看相关文件夹。









