import urllib.request


def load_data():
    url = "http://www.baidu.com/"
    # get请求
    # http请求
    # response:http相应的对象
    response = urllib.request.urlopen(url)
    # 读取内容
    data = response.read()
    str_data = data.decode("utf-8")
    print(str_data)
    #将数据写入文件 超文本写入用字符串 视频音频用wb
    with open("baidu.html","w",encoding="utf-8") as f:
        f.write(str_data)

load_data()
