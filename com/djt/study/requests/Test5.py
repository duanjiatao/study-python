import requests


def test_bs4():
    url = 'https://www.baidu.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35'
    }
    response = requests.get(url=url, headers=headers)
    write_html(response)
    html = str(response.text.encode(response.encoding))
    print(html)


def write_html(response: requests.Response):
    with open(r'C:\Users\duanjiatao\Desktop\xxx.html', 'w', encoding=response.encoding) as file:
        file.write(response.text)
