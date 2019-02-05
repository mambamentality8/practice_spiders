#先安装第三方模块 requests
#pip install requests

import requests

url = "http://www.baidu.com"
response = requests.get(url)

#content属性 返回的类型 是bytes
content_data = response.content.decode('utf-8')
#content属性 返回的类型 是str
"""
   Content of the response, in unicode.

    If Response.encoding is None, encoding will be guessed using
    ``chardet``.
    
    python3字符串默认就是unicode
"""

text_data = response.text
print(text_data)
