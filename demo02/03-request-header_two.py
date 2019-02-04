import urllib.request


def load_baidu():
    url = "https://www.baidu.com"
    # 添加请求头信息
    header = {
        # 浏览器的版本
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"
    }

    # 创建请求对象(添加headers方式一)
    #request = urllib.request.Request(url, headers=header)
    # 创建请求对象(添加headers方式二)
    request = urllib.request.Request(url)
    request.add_header("User-Agent","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36")

    final_url = request.get_full_url()
    print(final_url)
    # 请求网络数据
    response = urllib.request.urlopen(request)
    data = response.read().decode("utf-8")

    # 第一种获取请求头的信息
    request_headers1 = request.headers
    # print(request_headers1)

    # 第二种获取请求头的信息(首字母大写,其他字母小写)
    request_headers2 = request.get_header("User-agent")
    # print(request_headers2)

    # 将数据写入文件 超文本写入用字符串 视频音频用wb
    with open("load_baidu.html", "w", encoding="utf-8") as f:
        f.write(data)


load_baidu()
