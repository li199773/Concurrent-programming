# `Concurrent-programming-python` 并发编程
# 总结：线程，进程，协程
## 1.线程的创建：
### 方式一：直接进行创建：
        t = threading.Thread(target=, args=(,))  # 逗号,传入的是一个元祖
        t.start()
### 方式二：使用类进行创建：
        class My_Thread(threading.Thread): #
            def __init__(self, filename):  # 定义初始化的方法
                # 必要进行还要处理父类
                # 方式一：直接进行调用即可
                # threading.Thread.__init__(self)
                # 方法二：使用super()方法
                super().__init__()
                self.filename = filename













