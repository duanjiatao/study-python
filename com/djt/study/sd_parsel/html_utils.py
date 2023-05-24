def write_html(path, resp):
    """
    将响应页面写入文件
    :param path:保存路径
    :param resp:请求响应
    :return:
    """
    with open(path, 'w', encoding=resp.encoding) as file:
        file.write(resp.text)
