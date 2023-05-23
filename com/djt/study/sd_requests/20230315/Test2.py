import requests

url = 'https://www.baidu.com'
headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

# 在请求头中带上User-Agent，模拟浏览器发送请求
response = requests.get(url, headers=headers)
print(response.status_code)
print(response.content)
# 打印请求头信息
print(response.request.headers)
