"""
需求：获取腾讯招聘的前100页的信息
"""
# 单线程：
import requests
import csv

# 文件写入的方式一：
# f = open("tencent_Single_thread.csv", 'a', encoding='utf-8', newline="")
# csv_write = csv.writer(f)
# csv_write.writerow(["工作岗位", "工作国家", "工作地点", "岗位名称"])

# 写入方式二：
headers = ["工作岗位", "工作国家", "工作地点", "岗位名称"]
with open('test2.csv', 'w', newline='', encoding='utf-8') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    # 定义基础的url
    base_url = "https://careers.tencent.com/tencentcareer/api/post/Query?"
    # 定义参数字典：
    params = {
        "keyword": "Go",
        "pageSize": "10",
        "language": "zh-cn",
        "area": "cn",
    }
    # 定义请求头：
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
    }
    # 循环遍历：
    for page in range(1, 100):
        params['pageIndex'] = page
        # 发起请求，接收返回
        resp = requests.get(url=base_url, headers=headers, params=params)
        # print(resp.json()) # 将其直接转移成json格式的输出
        # 获取相应的内容：
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
            # print(dic)
            dic["工作岗位"] = dic.pop("RecruitPostName")
            dic["工作国家"] = dic.pop("CountryName")
            dic["工作地点"] = dic.pop("LocationName")
            dic["岗位名称"] = dic.pop("CategoryName")

            # print(content)
            # print(dic)
            # 写入方式
            # 方式一：
            f_csv.writerows([dic])
            # print(RecruitPostName, CountryName, LocationName, CategoryName)
            # 方式二：
            # csv_write.writerow([RecruitPostName, CountryName, LocationName, CategoryName])
            pass
        print("第{}页下载成功".format(page))
