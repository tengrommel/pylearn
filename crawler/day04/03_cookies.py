"""
    获取 个人中心的页面

    1. 代码登录  登录成功 cookie(有效)
    2. 自动带着cookie 去请求个人中心
    cookiejar 自动保存这个cookie
"""

import urllib.request
from http import cookiejar
from urllib import parse

login_url = 'https://www.yaozh.com/login'
# 1.2 登录的参数
login_form_data = {
    "username": "xiaomaoera12",
    "pwd": "lina081012",
    "formhash": "CE3ADF28C5",
    "backurl": "https%3A%2F%2Fwww.yaozh.com%2F"
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
    ,
    'Cookie': '_ga=GA1.2.1820447474.1535025127; MEIQIA_EXTRA_TRACK_ID=199Tty9OyANCXtHaSobJs67FU7J; UtzD_f52b_ulastactivity=1511944816%7C0; WAF_SESSION_ID=7d88ae0fc48bffa022729657cf09807d; PHPSESSID=7jsc60esmb6krgthnj99dfq7r3; _gid=GA1.2.358950482.1540209934; _gat=1; MEIQIA_VISIT_ID=1BviNX3zYEKVS7bQVpTRHOTFV8M; yaozh_logintime=1540209949; yaozh_user=381740%09xiaomaoera12; yaozh_userId=381740; db_w_auth=368675%09xiaomaoera12; UtzD_f52b_saltkey=CfYyYFY2; UtzD_f52b_lastvisit=1540206351; UtzD_f52b_lastact=1540209951%09uc.php%09; UtzD_f52b_auth=2e13RFf%2F3R%2BNjohcx%2BuoLcVRx%2FhF0NvwUbslgSZX%2FOUMkCRRcgh5Ayg6RGnklcG3d2DkUFAXJxjhlIS8fPvr9rrwa%2FY; yaozh_uidhas=1; yaozh_mylogin=1540209953; MEIQIA_EXTRA_TRACK_ID=199Tty9OyANCXtHaSobJs67FU7J; WAF_SESSION_ID=7d88ae0fc48bffa022729657cf09807d; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1535025126%2C1535283389%2C1535283401%2C1539351081%2C1539512967%2C1540209934; MEIQIA_VISIT_ID=1BviNX3zYEKVS7bQVpTRHOTFV8M; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1540209958'
}

# 1.3 发送登录请求POST
cook_jar = cookiejar()
cook_handler = urllib.request.HTTPCookieProcessor(cookiejar)
# 根据处理器生成opener
opener = urllib.request.build_opener(cook_handler)
# 1.参数 将来 需要转译 转码; 2. post请求的 data要求是bytes
login_str = parse.urlencode(login_form_data).encode('utf-8')
# 带着参数发送post请求
login_request = urllib.request.Request(login_url, headers=headers, data=login_str)

# 2. 代码带着cooke去访问 个人中心
center_url = 'https://www.yaozh.com/member/'

center_request = urllib.request.Request(center_url, headers=headers)
response = opener.open(center_url)

data = response.read().decode()

with open('02_cookies.html', 'w') as f:
    f.write(data)