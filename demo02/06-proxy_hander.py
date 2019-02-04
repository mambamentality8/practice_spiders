import urllib.request


def create_proxy_handler():
    url = "https://www.cnblogs.com/zrmw/p/9332801.html"

    # 添加代理
    proxy = {
        # 免费代理两种写法
        # "http":"http://182.111.64.7:41766"
        "http": "182.111.64.7:41766"
    }

    # 创建处理器
    proxy_handler = urllib.request.ProxyHandler(proxy)
    # 创建opener
    opener = urllib.request.build_opener(proxy_handler)

    data = opener.open(url).read()
    print(data)


create_proxy_handler()
