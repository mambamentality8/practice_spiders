import urllib.request

"""
HTTPError继承了URLError
"""
url = 'https://blog.csdn.net/rx3oyuyi/article/details/999999999'
url = 'http:/www.asdjfsa.cn'

try:
    response = urllib.request.urlopen(url)
except urllib.request.HTTPError as error:
    print(error.code)
except urllib.request.URLError as error:
    print(error)
