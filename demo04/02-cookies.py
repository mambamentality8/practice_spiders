"""
    直接获取 个人中心的页面
    手动 复制 PC 抓包的 cookies
    放在 request对象的请求头里面
    
"""
import urllib.request
import ssl

# 测试时报错：urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed
ssl._create_default_https_context = ssl._create_unverified_context

# 1.数据url
url = "https://www.yaozh.com/member/"

# 2.添加请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',

    'Cookie': 'acw_tc=707c9fcd15492515945672748e4b631fc8937a68fbf5495ea6f96e54db4603; yaozh_logintime=1549251930; yaozh_user=690433%09hello_world1; yaozh_userId=690433; db_w_auth=636795%09hello_world1; UtzD_f52b_saltkey=B33cFs4k; UtzD_f52b_lastvisit=1549248331; UtzD_f52b_lastact=1549251931%09uc.php%09; UtzD_f52b_auth=92ealpfN3RuAWnKC5pyxB%2BzNsYHIs9%2BfEhoEry7t9oCobXrnCAaV2S%2BWNjWxdwJyZm5gKRtoZmy%2FxLTuL33JOh7gsXA; yaozh_uidhas=1; yaozh_mylogin=1549251933; acw_tc=707c9fcd15492515945672748e4b631fc8937a68fbf5495ea6f96e54db4603; MEIQIA_VISIT_ID=1GhJUc8dvYVS1f4VOPiqHXXDTuI; MEIQIA_EXTRA_TRACK_ID=1GhJUbtfXfSZJTWio9KfJk09VL9; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1549251913%2C1549251951; PHPSESSID=osklf3l4cv2b5t48s1jqmclnh4; MEIQIA_VISIT_ID=1GhJUc8dvYVS1f4VOPiqHXXDTuI; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1549251988'
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
