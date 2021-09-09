import threading

lock = threading.Lock()  # 创建锁的方法
a = 0  # a是一个全局变量，是一个数值类型的值，数值类型是不可变的


def main():
    global a
    # b = a  # 或者传一个值进行接收
    # 在局部变量中对全局变量中进行修改的话，必须要用global

    # 解决出现的问题：上锁即可
    lock.acquire()
    for i in range(1000000):  # 位数很小的情况下无所谓，但是位数很大的情况下容易出现错误
        a += 1
    print(a)
    # 进行解锁，问题主要还是循环的问题 加锁之后必须要进行解说，不然会变成死锁
    lock.release()


if __name__ == '__main__':
    for i in range(2):
        t = threading.Thread(target=main)
        t.start()
