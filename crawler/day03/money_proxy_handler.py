import urllib.request


def money_proxy_use():
    use_name = "abc"
    pwd = "12345678"
    proxy_money = "123.158.63.130:8888"
    password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_manager.add_password(None, proxy_money, use_name, pwd)
    handle_auth_proxy = urllib.request.ProxyBasicAuthHandler(password_manager)
    opener_auth = urllib.request.build_opener(handle_auth_proxy)
    response = opener_auth.open("http://www.baidu.com")
    print(response.read())


if __name__ == '__main__':
    money_proxy_use()