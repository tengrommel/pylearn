import requests

url = 'http://www.baidu.com'
response = requests.get(url)
data = response.content
print(data)