# -*- coding: utf-8 -*-
# @Time : 2021/12/9 15:25
# @Author : O·N·E
# @File : 02 进程的创建.py
"""
进程创建的两种方式
"""
from multiprocessing import Process
import time
import os


def func(content):
    print("{}输入完成".format(content))
    time.sleep(3)
    print("{}输出完成".format(content))


if __name__ == '__main__':
    """子进程依赖于主进程进行创建和输出"""
    p = Process(target=func, args=(123,))
    p.start()  # 给操作系统发信号开启子进程需要时间，还是阻塞的状态，先执行主进程
    print("321")  # 这是主进程 会先打印它的输出
    print("父进程{}".format(os.getpid()))
    print("子进程{}".format(os.getppid()))
    time.sleep(50)
