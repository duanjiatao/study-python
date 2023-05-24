import json
from urllib.parse import parse_qs, urlparse


def parse_url(url: str):
    """
    解码url
    :param url:
    :return:
    """
    print()
    parsed_url = urlparse(url)
    query = parsed_url.query

    # 解码查询字符串并将结果转换为字典形式
    params = parse_qs(query)
    print(params)
    print("=" * 100)
    params_json = json.dumps(params, indent=4, ensure_ascii=False)
    print(params_json)


def test_parse_url():
    url = 'https://mng-dev.jlpay.com/system/views/index.html?params=%7B%22access_token%22%3A%22eyJ0eXAiOiJKV1QiLCJwbGF0IjoiQUMiLCJhbGciOiJTTTNXaXRoU00yIn0.eyJzdWIiOiJQIiwidWlkIjoiMjAyMDAyMTc4MDA0MTY0OCIsIm5iZiI6MTY4NDM4ODI3MiwidW5hbWUiOiLmrrXkvbPmtpsiLCJpc3MiOiJKTFBBWSIsImV4cCI6MTY4NDQ3NDY3MiwiaWF0IjoxNjg0Mzg4MjcyLCJqdGkiOiIyMTMzMjUwNjQ4NzIyNzIxMXQwbkp1RTd5TncifQ.MEQCIAnJkBk3uQESu-Jq5r68tY19TKiQsgm5Mu64oYtA-icWAiB8cZubFvB1_u0dOQ7ZI7jKWJu04FQOdNgNDYsjPzlm1w%22%2C%22user_id%22%3A%222020021780041648%22%2C%22user_name%22%3A%22%E6%AE%B5%E4%BD%B3%E6%B6%9B%22%2C%22mobile%22%3A%22150****3321%22%2C%22lastLoginTime%22%3A%222023-05-18%2011%3A45%3A59%22%2C%22plat_code%22%3A%22manage%22%2C%22web_name%22%3A%22https%3A%2F%2Fmanage-dev.jlpay.com%22%7D'
    parse_url(url)
