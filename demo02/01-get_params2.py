import urllib.request
import urllib.parse
import string


def get_params():
    url = "http://www.baidu.com/s?"
    params = {
        "wd": "中文",
        "key": "zhang",
        "value": "san"
    }
    # 自动将字典里面的东西变成url参数格式
    str_params = urllib.parse.urlencode(params)
    final_url = url + str_params
    print(final_url)

    # 发起请求
    response = urllib.request.urlopen(final_url)
    data = response.read().decode("utf-8")
    print(data)

    # 将数据写入文件 超文本写入用字符串 视频音频用wb
    with open("get_params.html", "w", encoding="utf-8") as f:
        f.write(data)
get_params()
