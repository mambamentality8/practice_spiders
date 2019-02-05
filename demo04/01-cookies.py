import urllib.request
import ssl

# 测试时报错：urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed
ssl._create_default_https_context = ssl._create_unverified_context

# 1.数据url
url = "https://www.yaozh.com/member/"

# 2.添加请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

# 3.构建请求对象
request = urllib.request.Request(url, headers=headers)

# 4.发送请求对象
response = urllib.request.urlopen(request)

# 5.读取数据
data = response.read()

# 保存到文件中,验证数据
with open('01cookie.html', 'wb') as f:
    f.write(data)
