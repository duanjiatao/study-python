import re

import requests

url = 'https://www.baidu.com'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.43"
}
# 在请求头中带上User-Agent，模拟浏览器发送请求
response = requests.get(url, headers=headers)
print(response.content)
# 打印请求头信息
print(response.request.headers)

response = requests.get('https://www.zhihu.com/explore', headers=headers)
result = re.findall("(ExploreSpecialCard-contentTitle|ExploreRoundtableCard questionTitle).*?>(.*?)</a>", response.text)
for i in result:
    print(i[1])

response = requests.get("https://github.com/favicon.ico")
with open('github.ico', 'wb') as f:
    f.write(response.content)
