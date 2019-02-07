import requests
from lxml import etree
import json
from bs4 import BeautifulSoup


class BookSpider(object):
    def __init__(self):
        self.session = requests.session()
        self.base_url = "http://www.allitebooks.com/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
        }
        self.data_list = []

    # 1.构建所有url
    def get_url_list(self):
        url_list = []
        for i in range(1, 2):
            url = self.base_url.format(i)
            url_list.append(url)
        return url_list

    # 发送请求
    def send_request(self, url):
        data = self.session.get(url, headers=self.headers).content.decode("gbk")
        return data

    # 3.解析数据 xpath
    def parse_xpath_data(self, data):
        parse_data = etree.HTML(data)

        # 1.解析出所有的书
        book_list = parse_data.xpath('//*[starts-with(@id, "post-")]')
        # 2.解析出每本书的信息
        for book in book_list:
            book_dict = {}
            # 1.书名
            book_dict["book_name"] = book.xpath('.//h2[@class="entry-title"]/a/text()')[0]
            # print(book_name)
            # 2.书的图片的url
            book_dict["book_img_url"] = book.xpath('div[@class="entry-thumbnail hover-thumb"]/a/img/@src')[0]
            # print(book_img_url)
            # 3.书的作者
            book_dict["book_author"] = book.xpath('.//h5[@class="entry-author"]/a/text()')[0]
            # print(book_author)
            # 4.书的简介
            book_dict["book_info"] = book.xpath('.//div[@class="entry-summary"]/p/text()')[0]
            # print(book_info)

            self.data_list.append(book_dict)

    def parse_bs4_data(self, data):
        # 1.取出所有的书
        bs4_data = BeautifulSoup(data, "lxml")
        book_list = bs4_data.select('article')
        print(len(book_list))
        for book in book_list:
            book_dict = {}
            # 1.书名
            book_dict["book_name"] = book.select_one('.entry-title').get_text()
            print(book_dict)
            # 2.书的图片的url
            # book_dict["book_img_url"] = book.xpath('div[@class="entry-thumbnail hover-thumb"]/a/img/@src')[0]
            # print(book_img_url)
            # 3.书的作者
            # book_dict["book_author"] = book.xpath('.//h5[@class="entry-author"]/a/text()')[0]
            # print(book_author)
            # 4.书的简介
            # book_dict["book_info"] = book.xpath('.//div[@class="entry-summary"]/p/text()')[0]
            # print(book_info)

            self.data_list.append(book_dict)

    # 4.保存数据
    def save_data(self):
        json.dump(self.data_list, open('01-book.json', 'w'))

    # 统筹调用
    def start(self):
        url_list = self.get_url_list()

        # 循环遍历发送请求
        for url in url_list:
            data = self.send_request(url)
            # self.parse_xpath_data(data)
            self.parse_bs4_data(data)
        self.save_data()


BookSpider().start()
