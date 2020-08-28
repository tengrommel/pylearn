import urllib.request


def load_baidu():
    url = "https://www.baidu.com"
    # 创建请求对象
    request = urllib.request.Request(url)
    # 请求网络数据
    response = urllib.request.urlopen(url)
    print(response)
    data = response.read().decode("utf-8")

    # 获取响应头
    # print(response.headers)
    request_headers = request.headers
    print(request_headers)
    with open("02header.html", "w") as f:
        f.write(data)


if __name__ == '__main__':
    load_baidu()