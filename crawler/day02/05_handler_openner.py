import urllib.request


def handler_opener():
    # 系统的urlopen并没有添加代理功能，所以需要我们自定义
    # 安全 套接层 ssl第三方的CA数字证书
    # http和https 80 443
    # urlopen 为什么可以请求数据 handler处理器
    # 自己的opener请求数据
    # urllib.request.urlopen()
    url = "https://blog.csdn.net/m0_37499059/article/details/79003731"
    # 创建自己的处理器
    handler = urllib.request.HTTPHandler()
    # 创建自己的openner
    opener = urllib.request.build_opener(handler)
    # 用自己创建的opener调用open方法
    response = opener.open(url)
    data = response.read()
    print(response)
    print(data)


if __name__ == '__main__':
    handler_opener()