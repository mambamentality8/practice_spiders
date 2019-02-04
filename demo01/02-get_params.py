import urllib.request
import urllib.parse
import string


def get_method_params():
    # 拼接字符串(汉字)
    url = "http://www.baidu.com/s?wd="

    name = "美女"
    final_url = url + name
    # 将包含汉字的请求进行url编码
    encode_new_url = urllib.parse.quote(final_url, safe=string.printable)
    print(encode_new_url)

    response = urllib.request.urlopen(encode_new_url)
    print(response)
    # UnicodeEncodeError: 'ascii' codec can't encode characters in position 10-11: ordinal not in range(128)
    # python是解释性语言;解析器只支持ascii 0 - 127

    #解码
    data = response.read()
    str_data = data.decode("utf-8")
    print(str_data)


    #将数据写入文件
    with open("02-encode.html","w",encoding="utf-8") as f:
        f.write(str_data)
get_method_params()
