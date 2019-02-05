import requests

url = 'https://www.12306.cn/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
}
#verify 告诉web忽略证书访问
response = requests.get(url=url, headers=headers, verify=False)
data = response.content.decode()

with open('02-ssl.html', 'w', encoding='utf-8') as f:
    f.write(data)
