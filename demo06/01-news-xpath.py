import requests

from lxml import etree

session = requests.session()
url = "http://news.baidu.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
}

data = session.get(url, headers=headers, ).content.decode()
print(type(data))
# 1.转解析类型
xpath_data = etree.HTML(data)
print(type(xpath_data))
# 2.调用xpath的方法
# xpath的各种语法在这里不详细讲解了
result = xpath_data.xpath('')
