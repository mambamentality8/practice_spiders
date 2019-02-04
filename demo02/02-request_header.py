import urllib.request


def load_baidu():
    url = "http://www.baidu.com"

    # 创建请求对象
    request = urllib.request.Request(url)

    # 请求网络数据
    response = urllib.request.urlopen(request)
    print(response)
    data = response.read().decode("utf-8")

    # 获取请求头的信息
    request_headers = request.headers
    print(request_headers)

    # 将数据写入文件 超文本写入用字符串 视频音频用wb
    with open("load_baidu.html", "w", encoding="utf-8") as f:
        f.write(data)
load_baidu()
