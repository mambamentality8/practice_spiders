import urllib.request


def random_user_proxy():
    url = "https://www.cnblogs.com/zrmw/p/9332801.html"

    # 添加代理
    proxy_list = [
        {"http": "182.111.64.7:41766"},
        {"http": "1.192.243.134:9797"},
        {"http": "121.69.37.6:9797"},
        {"http": "36.110.234.244:80"},
        {"http": "180.141.90.172:53281"},
    ]

    for proxy in proxy_list:
        print(proxy)
        proxy_handler = urllib.request.ProxyHandler(proxy)
        opener = urllib.request.build_opener(proxy_handler)
        try:
            opener.open("https://www.baidu.com")
            print("xxx")
        except Exception as e:
            print(e)

random_user_proxy()
