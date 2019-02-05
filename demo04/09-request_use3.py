import requests


# 参数 自动转移
url = "https://www.baidu.com/s"
params = {
    'wd': "你好"
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
response = requests.get(url, headers=headers, params=params)

data = response.content.decode()

with open('09-request.html', 'w', encoding="utf-8") as f:
    f.write(data)


#发送POST 和添加参数
# requests.post(url,data=(字典),json=(字符串))