# -*- coding: utf-8 -*-
# @Time : 2021/12/17 16:28
# @Author : O·N·E
# @File : 01 理论,线程开启的两种方式.py
"""
理论：
    1.进程是资源单元，线程是执行单位
    开启一个进程，进程会在内存中开辟一个空间，将主进程中的内容复制一份，然后交给线程去执行
    2.线程开启的速度非常快，消耗的资源非常小
"""
from threading import Thread


def main():
    print("one is all")


if __name__ == '__main__':
    t1 = Thread(target=main)
    t1.start()  # 速度非常快，相比与进程来说
    print(2)  # 子线程先进行打印，然后在进行打印主进程 进程还学要在内存中开辟一些空间，速度很慢
