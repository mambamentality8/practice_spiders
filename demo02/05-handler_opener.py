import urllib.request


def handler_openner():
    # 系统的urlopen并没有添加代理的功能所以需要我们自定义这个功能
    url = "https://www.cnblogs.com/zrmw/p/9332801.html"

    # 这个处理器不能添加代理
    handler = urllib.request.HTTPHandler()
    opener = urllib.request.build_opener(handler)

    response = opener.open(url)
    data = response.read().decode("utf-8")

    # 将数据写入文件 超文本写入用字符串 视频音频用wb
    with open("handler_openner.html", "w", encoding="utf-8") as f:
        f.write(data)

handler_openner()