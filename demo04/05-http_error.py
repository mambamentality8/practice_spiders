import urllib.request
"""
    urllib.error.HTTPError: HTTP Error 404: Not Found
"""
url = 'https://blog.csdn.net/rx3oyuyi/article/details/999999999'

response = urllib.request.urlopen(url)