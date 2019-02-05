import requests

# session类可以自动保存cookie相当于cookie_jar
session = requests.session()
# 请求数据url
member_url = "https://www.yaozhi.com/member/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
}

# 1.代码登陆
login_url = "https://www.yaozh.com/login"
login_form_data = {
    "username": "",
    "pwd": "",
    "formhash": "EF4F19F70C",
    "backurl": "https%3A%2F%2Fdb.yaozh.com%2F"
}

login_response = session.post(login_url, data=login_form_data,verify=False)

# 2.登陆成功之后 带着 有效的cookies 访问请求目标数据
data = session.get(member_url, headers=headers,verify=False).content.decode()

with open('04-cookie.html', 'w') as f:
    f.write(data)
