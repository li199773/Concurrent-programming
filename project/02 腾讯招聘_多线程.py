import requests
import threading
import csv
import time
from queue import Queue


# 定义生产者 作用：访问页面，获取数据，发起请求
class Productor(threading.Thread):
    # 覆写run方法
    def __init__(self, url_queue, content_queue):
        super().__init__()
        self.url_queue = url_queue
        self.content_queue = content_queue

    # 从队列里面取出url
    def run(self):
        while True:
            if self.url_queue.empty():
                break
            # 从队列里面取出url
            url = self.url_queue.get()
            self.url_resp(url)

    def url_resp(self, url):
        # 定义请求头：
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
        }
        resp = requests.get(url=url, headers=headers)
        # 获取相应的内容：
        time.sleep(0.5)
        Posts = resp.json()['Data']['Posts']
        for post in Posts:
            dic = {}
            RecruitPostName = post['RecruitPostName']
            CountryName = post['CountryName']
            LocationName = post['LocationName']
            CategoryName = post['CategoryName']
            dic["RecruitPostName"] = RecruitPostName
            dic["CountryName"] = CountryName
            dic["LocationName"] = LocationName
            dic["CategoryName"] = CategoryName
            # print(RecruitPostName, CountryName, LocationName, CategoryName)
            # 将数据插入到队列中去
            self.content_queue.put(dic)


# 定义消费者 保存的作用
class Consumer(threading.Thread):
    def __init__(self, url_queue, content_queue):
        super().__init__()
        self.url_queue = url_queue
        self.content_queue = content_queue

    def run(self):
        while True:
            if self.url_queue.empty() and self.content_queue.empty() and switch == 1:
                break
            try:
                content = self.content_queue.get(timeout=3)
                # f = open("tencent_Single_thread.csv", 'a', encoding='utf-8', newline="")
                # csv_write = csv.writer(f)
                # csv_write.writerow([content["RecruitPostName"], content["CountryName"], content["LocationName"],
                #                     content["CategoryName"]])
                data = content["RecruitPostName"] + "," + content["CountryName"] + "," + content["LocationName"] + "," + \
                       content[
                           "CategoryName"]
                print(data)
                fp.write(data + "\n")
                print("下载成功")
            except:
                break


def main():
    switch = 0
    # 定义基础的url，url不确定
    base_url = "https://careers.tencent.com/tencentcareer/api/post/Query?keyword=Go&pageIndex={}&pageSize=10&language=zh-cn&area=cn"
    # 定义存放的队列
    url_queue = Queue()  # 队列设置为无限大即可
    content_queue = Queue()
    # 循环遍历得到99页的数据
    for i in range(1, 100):
        url_list = base_url.format(i)
        # print(url_list)
        url_queue.put(url_list)
    # 定义生产者的列表:
    lists = []
    for i in range(10):
        productor = Productor(url_queue, content_queue)
        productor.start()
        lists.append(productor)
    for j in range(10):
        consumer = Consumer(url_queue, content_queue)
        consumer.start()
    # 阻塞每一个生产者:
    for list in lists:
        list.join()
    # 改变开关的值
    switch = 1


if __name__ == '__main__':
    # f = open("tencent_Multithreading.txt", 'a', encoding='utf-8', newline="")
    # csv_write = csv.writer(f)
    # csv_write.writerow(["工作岗位", "工作国家", "工作地点", "岗位名称"])
    # main()

    with open("tencent_Multithreading_text.txt", 'a', encoding='utf-8') as fp:
        main()
