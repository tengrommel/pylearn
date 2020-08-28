# 请求

- 1、get 传参
    - （1）汉字报错：解释器ascii没有汉字url汉字转码
    > urllib.parse.quote string safe="string.printable"
    
    - （2）字典传参
    > urllib.parse.urlencode()

- 2、post 传参
> urllib.request.openurl(url, data="服务器接受的数据")

handle：处理器的自定义

User-Agent:
> 模拟真实的浏览器返送请求：
- （1）百度批量搜索
- （2）检查元素
- （3）request.add_header(动态添加head数据)

ip代理
- 免费的IP 时效性差，错误率高
- 付费的IP 

