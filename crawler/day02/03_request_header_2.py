import urllib.request


def load_baidu():
    url = "https://www.baidu.com"
    # 添加请求头的信息
    header = {
        # 浏览器的版本
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "ha": "he"
    }
    # 创建请求对象
    request = urllib.request.Request(url)
    request.add_header("user-agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36")
    # 请求网络数据
    response = urllib.request.urlopen(request)
    print(response)
    data = response.read().decode("utf-8")

    # 获取到完整的url
    final_url = request.get_full_url()
    print(final_url)
    # 获取响应头
    # print(response.headers)
    # request_headers = request.headers
    # print(request_headers)
    # 第二种方式打印headers的信息
    request_headers = request.get_header("User-agent")
    print(request_headers)
    with open("02header.html", "w") as f:
        f.write(data)


if __name__ == '__main__':
    load_baidu()
