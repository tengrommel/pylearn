import urllib.request
import urllib.parse
import string


def get_params():
    url = "http://www.baidu.com/s?"
    params = {
        "wd": "中文",
        "key": "zhang",
        "value": "san"
    }
    str_params = urllib.parse.urlencode(params)
    print(str_params)
    final_url = url + str_params
    # 将带有中文的url转移成计算机可以识别的
    end_url = urllib.parse.quote(final_url, safe=string.printable)
    response = urllib.request.urlopen(end_url)
    data = response.read().decode("utf-8")
    print(data)


if __name__ == '__main__':
    get_params()