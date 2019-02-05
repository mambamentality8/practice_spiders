"""
    直接获取 个人中心的页面
    1.代码登录 登录成功 cookie(有效)
    2.自动带着cookie去请求个人中心
    cookiejar自动保存cookie
"""
import urllib.request
from http import cookiejar
import ssl
from urllib import parse

# 测试时报错：urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed
ssl._create_default_https_context = ssl._create_unverified_context

# 登录之前的 登录页的网址https://www.yaozh.com/login
# 找登录参数

# 后台 根据你发送的请求方式来判断的 如果你发送的是get返回登录页面,如果是POST登录返回登陆结果

# 1.代码登录
# 1.1 登陆的网址
login_url = "https://www.yaozh.com/login"
# 1.2 登陆的参数
login_from_data = {
    "username": "15510050030",
    "pwd": "hsw123456**",
    "formhash": "0F4D8726B6",
    "backurl": "%2F%2Fwww.yaozh.com%2F"
}
# 1.3 发送POST登陆请求
cookie_jar = cookiejar.CookieJar()
# 定义有添加 cookie 功能的处理器
cookie_handler = urllib.request.HTTPCookieProcessor(cookie_jar)
# 根据处理器 生成opener
opener = urllib.request.build_opener(cookie_handler)
# 带着参数 发送post请求
# 2.添加请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
#将字典转换成url编码
login_str = parse.urlencode(login_from_data).encode("utf-8")
login_request = urllib.request.Request(login_url, headers=headers, data=login_str)
# 如果登陆成功,cookie_jar自动保存cookie
opener.open(login_request)

# 2.代码带着cooike去访问个人中心
member_url = "https://www.yaozh.com/member/"
member_request = urllib.request.Request(member_url, headers=headers)
response = opener.open(member_request)
data = response.read().decode("utf-8")

# 写入本地文件
with open('03-cookie.html', 'w', encoding="utf-8") as f:
    f.write(data)
