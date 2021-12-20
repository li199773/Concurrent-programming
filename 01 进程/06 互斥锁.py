# -*- coding: utf-8 -*-
# @Time : 2021/12/17 9:36
# @Author : O·N·E
# @File : 06 互斥锁.py
"""
1.类似于公司打印机情况，有三个用户使用打印机，即使同时上传内容到打印机，打印机也会按照顺序进行打印
"""
from multiprocessing import Process
from multiprocessing import Lock
import time
import random


def task(a, lock):
    lock.acquire()  # 上锁
    print("{}开始执行任务".format(a))
    time.sleep(random.randint(1, 3))
    print("{}结束任务".format(a))
    lock.release()  # 解锁


if __name__ == '__main__':
    list = []
    mutex = Lock()  # 谁先抢到谁先上锁，都是同一把锁
    for i in range(1, 10):
        p = Process(target=task, args=(i, mutex))
        list.append(p)
        p.start()  # 输出很乱，跟现实中打印文件结果不一样子

"""
    lock与jion的区别：
    共同点：都可以把并发变成串行，保证顺序性
    不同点：jion为人为设定,lock让cpu去决定顺序，保证公平性。
"""
