"""
创建Queue对象:(先进先出)
maxsize设置队列中最大的存入量
"""
from queue import Queue

q = Queue(maxsize=4)
# 元素的存入
q.put(1)
q.put(2)
q.put(3)
# q.put(4)
q.put(5)  # 设置最大的存入量之后 在进行插入之后不会报错，会在1取出之后在进行插入操作
# 进入阻塞的状态
# 元素的取出
print(q.get())
print(q.get())
print(q.get())
print(q.get())  # 先进先出的规则进行输出

# 队列在爬虫中的使用
# 1.将爬取的url存放到队列中，每次生产者进行爬取的时候，会从队列中取出url进行请求
# 2.将生产者爬取到的数据存放到队列中，消费者从队列中取出数据，保存即可
