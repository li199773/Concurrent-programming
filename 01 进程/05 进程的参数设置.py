# -*- coding: utf-8 -*-
# @Time : 2021/12/16 16:32
# @Author : O·N·E
# @File : 05 进程的参数设置.py
from multiprocessing import Process
import time


def main(number):
    print("{} running".format(number))
    time.sleep(2)
    print("{} gone".format(number))


if __name__ == '__main__':
    p = Process(target=main, args=(123,))
    p.start()
    p.terminate()  # 杀死进程的意思，进程不执行，直接执行主程序

    """
    即使上面是杀死进程的命令，但是也是很快执行主程序，在杀死之前就已经执行判断是否活着的命令
    可以选择睡眠时间，等待命令杀死进程
    """
    time.sleep(2)
    print(p.is_alive())
    print("主进程开始打印")
