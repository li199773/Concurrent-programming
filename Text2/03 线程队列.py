# -*- coding: utf-8 -*-
# @Time : 2021/12/9 11:04
# @Author : O·N·E
# @File : 03 线程队列.py
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
