# -*- coding: utf-8 -*-
# @Time : 2021/12/17 15:19
# @Author : O·N·E
# @File : 08 生产者消费者模式.py
from multiprocessing import Process
from multiprocessing import Queue
import time
import random


def product(q):
    for i in range(100):
        time.sleep(1)
        res = random.randint(1, 10)
        q.put(res)
        print("用户{}生产了{}".format(i, res))


def consumer(q):
    try:
        for i in range(100):
            time.sleep(1)
            q.get()
            print("用户{}消费了{}".format(i, q.get()))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=product, args=(q,))
    p2 = Process(target=consumer, args=(q,))
    p1.start()
    p2.start()
