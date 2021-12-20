# -*- coding: utf-8 -*-
# @Time : 2021/12/17 11:06
# @Author : O·N·E
# @File : 07 进程之间的通信.py
"""
进程之间的通信:
    1.基于文件之间的通信
    2.基于队列之间的通信
    3.基于管道之间的通信
"""
from multiprocessing import Process
from multiprocessing import Lock
import random
import time
import json
import os


# demo1 基于文件之间的通信
# 设计一个抢票的系统 首先先查剩余的票数，剩余的票数可以一起看是并行，买票是串行
def check():
    time.sleep(random.randint(1, 3))
    with open("ticket.json", encoding="utf-8") as fp:
        dic = json.load(fp)
        print("{}查看剩余的票为{}".format(os.getpid(), dic["ticket"]))


def buy():
    with open("ticket.json", encoding="utf-8") as fp:
        dic = json.load(fp)
    if dic["ticket"] > 0:
        dic["ticket"] -= 1
        time.sleep(random.randint(1, 3))
        with open("ticket.json", "w", encoding="utf-8") as fp:
            json.dump(dic, fp)
        print("{}购买成功".format(os.getpid()))


def main(lock):
    check()
    lock.acquire()
    buy()
    lock.release()


if __name__ == '__main__':
    mutex = Lock()
    for i in range(6):
        p = Process(target=main, args=(mutex,))
        p.start()
# 容易出现死锁

# demo2 基于队列
"""
第一种，先进先出
"""
import queue

q = queue.Queue(maxsize=3)
q.put(1)
q.put(2)
q.put(3)
# q.put(4)  # 设置最大的队列数量为3，传入四个会造成队列阻塞
print(q.get())
print(q.get())
print(q.get())
# print(q.get(block=False))  # 取出四个会显示报错，不会进行报错

"""
第二种 先进后出
"""
q = queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)
print(q.get())
print(q.get())
print(q.get())

"""
优先级别输出 输入进去是一个元祖，按照大小进行输出，-1的优先级别要比0的优先接要搞
"""
q = queue.PriorityQueue()
q.put((0, "one"))
q.put((1, "two"))
q.put((-1, "three"))
print(q.get())
print(q.get())
print(q.get())
