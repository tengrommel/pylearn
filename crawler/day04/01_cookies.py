import urllib.request

# 1.数据url
url = 'https://www.yaozh.com/member/'
# 2.添加请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
data = response.read()

with open('01cook.html', 'w') as f:
    f.write(data)
