import json

import requests

# 1.创建url
url = "https://api.github.com/user"

# 2.添加请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
# 3.执行请求
response = requests.get(url, headers=headers)

###########方式一##############
# # 4.将响应数据解码
# data = response.content.decode()
# # 将字符串转换成字典
# data_dict = json.loads(data)
# print(data_dict['message'])


###########方式二##############
#json() 自动将json字符串 转换成python dict list
data = response.json()
print(type(data))
print(data['message'])