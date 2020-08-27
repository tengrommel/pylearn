import urllib.request


def load_data():
    url = "http://www.baidu.com/"
    # get的请求
    # http的请求
    # response: http响应的对象
    response = urllib.request.urlopen(url)
    print(response)
    # 读取内容 bytes类型
    data = response.read()
    print(data)
    # 将文件获取的内容转换成字符串
    str_data = data.decode("utf-8")
    print(str_data)
    # 数据写入文件
    with open("baidu.html", "w", encoding="utf-8") as f:
        f.write(str_data)


if __name__ == '__main__':
    load_data()
