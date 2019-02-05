import requests


# 请求数据url
member_url = "https://www.yaozhi.com/member/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
}
# 第一种方式用sublime将cookies转换成字典的形式
cookies = "acw_tc=2f624a4515492574786015136e62c619f5fe9e4ffd608224b615127645b7b1; think_language=zh-CN; _ga=GA1.2.410766714.1549277028; _gat=1; PHPSESSID=cuosh30k0u1fht5v8ctn9smh35; yaozh_userId=690433; UtzD_f52b_saltkey=KlLw3Vf2; UtzD_f52b_lastvisit=1549273436; yaozh_uidhas=1; yaozh_mylogin=1549277060; UtzD_f52b_ulastactivity=1549251106%7C0; yaozh_logintime=1549277096; yaozh_user=690433%09hello_world1; db_w_auth=636795%09hello_world1; UtzD_f52b_lastact=1549277098%09uc.php%09; UtzD_f52b_auth=c7de%2B1lXHxOsvWSzUfQWskHDb%2BdBCZ0AiERC8HCwc6QY4gO5hMDG9bw7GHvUPWpIwtq5gIB9P0trUw49NdDSdesxW3Y; acw_tc=2f624a4515492574786015136e62c619f5fe9e4ffd608224b615127645b7b1; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1549251913%2C1549251951%2C1549257479%2C1549277027; MEIQIA_VISIT_ID=1Gi8OuOfIW4Xcz0n2PNlMXWhJ0P; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1549289144; MEIQIA_VISIT_ID=1GiWxJbXDFmGt8C7BxOm27nAp0x"

# 需要的是字典类型
cook_dict = {}
cookies_list = cookies.split('; ')
for cookie in cookies_list:
    cook_dict[cookie.split('=')[0]] = cookie.split('=')[1]

#字典推导式
# cook_dict={cookie.split('=')[0]:cookie.split('=')[1] for cookie in cook_dict}
print(cook_dict)

response = requests.get(member_url, headers=headers, cookies=cook_dict)

data = response.content.decode()

with open('03-cookie.html','w') as f:
    f.write(data)
