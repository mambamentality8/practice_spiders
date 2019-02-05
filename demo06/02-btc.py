import requests
from lxml import etree
import json


class BtcSpider(object):
    def __init__(self):
        self.base_url = "http://8btc.com/forum-61-"
        self.session = requests.session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
        }
        self.data_list = []

    # 1.发送请求
    def get_response(self, url):
        response = self.session.get(url, headers=self.headers)
        # 网页的编码自动去猜
        data = response.text
        return data

    # 2.解析数据
    def parse_data(self,data):
        # 使用xpath 解析当前页面所有的新闻title和url保存
        # 1.转类型
        x_data = etree.HTML(data)
        # 2.根据xpath路径解析
        title_list = x_data.xpath('//a[@class="s xst"]/text()')
        url_list = x_data.xpath('//a[@class="s xst"]/@href')

        # 枚举遍历
        for index, title in enumerate(title_list):
            news = {}
            # print(index)
            # print(title)
            news['name'] = title
            news['url'] = url_list[index]
            self.data_list.append(news)


    # 3.保存数据
    def save_data(self):
        data_str = json.dumps(self.data_list)
        with open('02-btc.json', 'w') as f:
            f.write(data_str)

    # 4.启动
    def run(self):
        # 翻页
        for i in range(5):
            # 1.拼接 完整url
            page = str(i+1)
            url = self.base_url + page + ".html"
            # 2.发请求
            data = self.get_response(url)
            # 3.做解析
            parse_data = self.parse_data(data)
        # 4.保存
        self.save_data()


BtcSpider().run()
