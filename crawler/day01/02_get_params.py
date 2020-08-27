import urllib.request
import urllib.parse
import string


def get_method_params():
    url = "https://www.baidu.com/s?wd="
    # 拼接字符串（汉字）
    name = "美女"
    final_url = url + name
    print(final_url)
    # 使用代码发送网络请求
    # 网址里面包含了汉字；ascii是没有汉字的;url转译
    # 将包含汉字的网址进行转译
    encode_new_url = urllib.parse.quote(final_url, safe=string.printable)
    print(encode_new_url)
    response = urllib.request.urlopen(encode_new_url)
    print(response)
    # 读取内容
    data = response.read().decode()
    print(data)
    # 保存到本地
    with open("02_get_params.html", "w", encoding="utf-8") as f:
        f.write(data)

    # UnicodeEncodeError: 'ascii' codec can't encode
    # characters in position 10-11:
    # ordinal not in range(128)
    # python 是解释性语言，它的解析器只支持ascii 0-127
    # 不支持中文


if __name__ == '__main__':
    get_method_params()