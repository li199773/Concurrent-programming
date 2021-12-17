# -*- coding: utf-8 -*-
# @Time : 2021/12/16 14:52
# @Author : O·N·E
# @File : 04 join.py
from multiprocessing import Process
import time


# demo1
def main(str, sec):
    print("ONE{}".format(str))
    time.sleep(sec)


if __name__ == '__main__':
    start_time = time.time()
    process1 = Process(target=main, args=("爱中国", 1))
    process2 = Process(target=main, args=("爱祖国", 2))
    process3 = Process(target=main, args=("爱人民", 3))

    process1.start()  # 开启三个进程测试
    process2.start()
    process3.start()

    # p1 p2 p3其实是同一时间进行发出的
    process1.join()  # join方法就是主进程等待子进程结束之后才开始运行
    process2.join()
    process3.join()
    end_time = time.time()
    print(end_time - start_time)  # 算时间最长的，在加上一些开启线程的时间很，差不多是3秒多一些
    print("主进程开始运行")


# demo2 对上面的代码进行改进错误的示范
def main(i):
    print(i)
    time.sleep(i)


if __name__ == '__main__':
    start_time = time.time()
    for i in range(1, 4):  # 这是串行 不是并行，不跟上面那个一样子
        p1 = Process(target=main, args=(i,))
        p1.start()
        p1.join()  # join之后是每一个进程结束之后在开启下一个进程所以时间是之和
    end_time = time.time()
    print(end_time - start_time)

# demo3 正确的方法
def main(i):
    print(i)
    time.sleep(i)


if __name__ == '__main__':
    start_time = time.time()
    list = []
    for i in range(1, 100):
        p = Process(target=main, args=(i,))
        list.append(p)
        p.start()
    for p in list:
        p.join()  # jion就是阻塞意思，主进程等待jion完毕之后在进行执行
    end_time = time.time()
    print(end_time - start_time)
