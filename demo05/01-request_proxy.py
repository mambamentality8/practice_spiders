import requests


url = "http://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
}

freea_proxy = {"http":"116.209.56.64:9999"}

response = requests.get(url=url, headers=headers, proxies=freea_proxy)

print(response.status_code)
