"""
生产者和消费者模式：
假设有3个对象，生产者，银行，消费者，银行有1000w的存款，生产者有3个人，一边挣钱一边把钱存入银行，消费者有5人，一边花钱一边
将钱从银行里面取出来
"""
import threading
import random
import time

# 定义银行初始的钱数
chushi_money = 100
chushi_time = 0

# 定义锁
lock = threading.Lock()


# 生产者
class Productor(threading.Thread):
    # 覆写run方法
    def __init__(self, i):
        super().__init__()
        self.i = i

    def run(self):
        global chushi_money
        global chushi_time
        while True:  # 不会停止下去，会一直进行下去，现实中也是这样子的，生产者会一直进行生产下去
            # if chushi_time > 12:
            #     break
            lock.acquire()
            consumer_money = random.randint(100, 300)
            chushi_money += consumer_money
            chushi_time += 1
            print("{}挣了{},银行存款{}".format(self.i, consumer_money,chushi_money))
            lock.release()


# 消费者
class Consumer(threading.Thread):
    def __init__(self, i):
        super().__init__()
        self.i = i

    def run(self):
        global chushi_money
        while True:
            lock.acquire()
            consumer_money = random.randint(200, 300)
            chushi_money -= consumer_money
            if consumer_money > chushi_money:
                print("银行余额不足")
                lock.release()
                break
            print("{}花了{},银行余额为{}".format(self.i, consumer_money,chushi_money))

            lock.release()


if __name__ == '__main__':
    # 定义生产者消费者
    for i in range(1000):
        productor = Productor(i)

        consumer = Consumer(i)
        productor.start()
        consumer.start()
    # # 定义5个消费者
    # for j in range(5):
    #     consumer = Consumer(j)
    #     consumer.start()
