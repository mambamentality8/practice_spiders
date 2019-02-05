import requests


class RequestSpider(object):
    def __init__(self):
        url = "http://www.baidu.com"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        }
        self.response = requests.get(url, headers=headers)

    def run(self):
        data = self.response.content

        # 1.获取请求头
        requests_headers = self.response.request.headers
        #print(requests_headers)
        # 2.获取响应头
        response_headers = self.response.headers
        #print(response_headers)
        # 3.响应状态码
        code = self.response.status_code
        #print(code)
        # 4.请求的cookie
        request_cookie = self.response.request._cookies
        #print(request_cookie)
        # 5.相应的cookie
        response_cookie = self.response.cookies
        print(response_cookie)

RequestSpider().run()