import requests



class BookSpider(object):
    def __init__(self):
        self.session = requests.session()
        self.base_url = "http://www.allitebooks.com/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
        }

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
    def parse_xpath_data(self):
        pass

    # 4.保存数据
    def save_data(self, data):
        with open('book.html', 'w') as f:
            f.write(data)

    # 统筹调用
    def start(self):
        url_list = self.get_url_list()

        # 循环遍历发送请求
        for url in url_list:
            data = self.send_request(url)
            self.save_data(data)


BookSpider().start()
