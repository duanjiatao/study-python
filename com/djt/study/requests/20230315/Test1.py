import requests

url = 'http://httpbin.org/get'
# 生成get请求
rep = requests.get(url)
# 查看结果类型
print('查看结果类型：', type(rep))
# 查看状态码
print('状态码：', rep.status_code)
# 查看编码
print('编码：', rep.encoding)
# 查看响应头
print('响应头：', rep.headers)
# 打印查看网页内容
print('查看网页内容：', rep.text)

# GET请求
print(requests.get("http://httpbin.org/get").text)
# POST请求
print(requests.post("http://httpbin.org/post").text)
# PUT请求
print(requests.put("http://httpbin.org/put").text)
# DELETE请求
print(requests.delete("http://httpbin.org/delete").text)
# HEAD请求
print(requests.head("http://httpbin.org/get").text)
# OPTIONS请求
print(requests.options("http://httpbin.org/get").text)
