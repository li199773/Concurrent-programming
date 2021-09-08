import threading
import time
import random


# 方法一：
def download(filename):
    print(filename, "开始下载")
    time.sleep(random.randint(1, 5))  # 根据文件的大小随机进行随眠时间
    print(filename, "下载结束")


if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=download, args=(i,))  # 逗号,传入的是一个元祖
        t.start()


# 方法二：使用类进行创建多线程（使用的次数也是最多的）
# 步骤：
# 1.自定义一个类
# 2.继承Thread类
# 3.覆写run()方法，因为在多线程不进行覆写的话run()会调用父类的方法

class My_Thread(threading.Thread):
    def __init__(self, filename):  # 定义初始化的方法
        # 必要进行还要处理父类
        # 方式一：直接进行调用即可
        # threading.Thread.__init__(self)
        # 方法二：使用super()方法
        super().__init__()
        self.filename = filename

    def run(self):
        print(self.filename, "开始下载")
        time.sleep(random.randint(1, 5))
        print(self.filename, "结束下载")


if __name__ == '__main__':
    for i in range(10):
        thread = My_Thread(i)  # 传入参数，注意调用的是初始化方法
        thread.start()


# 2.线程的名字
class My_thread(threading.Thread):

    def run(self):
        print("{}正在运行".format(threading.current_thread()))  # 查看运行的进程的信息
        # name 属性可以查看线程的名称，默认的名称：Threading-n，n是一个数字
        print("{}正在运行".format(self.name))


if __name__ == '__main__':
    for i in range(10):
        t = My_thread(name="file{}".format(i))  # 可以传入线程名称，进行定义
        t.start()
