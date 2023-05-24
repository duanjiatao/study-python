import json

import requests


def test_cookies():
    """
    测试cookies
    :return:
    """
    url = 'https://mng-dev.jlpay.com/manage/dispatch/xdataquerydc'
    # cookies_str = 'experimentation_subject_id=IjFjY2Q2YzVjLTcwNWItNDA2OC04YWIwLTIzZDdjYTQ5N2M0MiI=--9ccaf4e2c4c9cbfa5d48c84e8d02ac0d2cf55b0c; MANAGE-FRONT-SESSION=234b2eb2-320c-4661-909f-97629fa8cdba; jlpay_access_token=eyJ0eXAiOiJKV1QiLCJwbGF0IjoiQUMiLCJhbGciOiJTTTNXaXRoU00yIn0.eyJzdWIiOiJQIiwidWlkIjoiMjAyMDAyMTc4MDA0MTY0OCIsIm5iZiI6MTY4Mzc2ODE2OCwidW5hbWUiOiLmrrXkvbPmtpsiLCJpc3MiOiJKTFBBWSIsImV4cCI6MTY4Mzg1NDU2OCwiaWF0IjoxNjgzNzY4MTY4LCJqdGkiOiIyMDcxMjQwMzA1MTI0MjEyMms5ZmhyQkxuVzcifQ.MEUCICTEdVT2UbN0xNqMjaf-hkd-GeFuQQme6ObeLNT-QtflAiEAz9Ha9jVIrFvIJIpTseZtv9FSCeytdAZm8v5ZlgmZc04'
    # cookies = {kv.split('=')[0]: kv.split('=')[1] for kv in cookies_str.split(';')}
    headers = {
        'platcode': 'manage',
        'Cookie': 'experimentation_subject_id=IjFjY2Q2YzVjLTcwNWItNDA2OC04YWIwLTIzZDdjYTQ5N2M0MiI=--9ccaf4e2c4c9cbfa5d48c84e8d02ac0d2cf55b0c; MANAGE-FRONT-SESSION=234b2eb2-320c-4661-909f-97629fa8cdba; jlpay_access_token=eyJ0eXAiOiJKV1QiLCJwbGF0IjoiQUMiLCJhbGciOiJTTTNXaXRoU00yIn0.eyJzdWIiOiJQIiwidWlkIjoiMjAyMDAyMTc4MDA0MTY0OCIsIm5iZiI6MTY4Mzc2ODE2OCwidW5hbWUiOiLmrrXkvbPmtpsiLCJpc3MiOiJKTFBBWSIsImV4cCI6MTY4Mzg1NDU2OCwiaWF0IjoxNjgzNzY4MTY4LCJqdGkiOiIyMDcxMjQwMzA1MTI0MjEyMms5ZmhyQkxuVzcifQ.MEUCICTEdVT2UbN0xNqMjaf-hkd-GeFuQQme6ObeLNT-QtflAiEAz9Ha9jVIrFvIJIpTseZtv9FSCeytdAZm8v5ZlgmZc04'
    }
    params = {
        'commandId': 'xdata_page_query_line',
        'access_key': 'risk.riskctrl',
        'offset': '0',
        'limit': '20',
        'key': 'queryMerchGradeStat',
        'queryParam': '{"beginDate": "20221124", "endDate": "20230222", "merchNoList": ["84944035812S123"]}'
    }

    response = requests.get(url=url, headers=headers, params=params)
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))


def test_save_html():
    url = 'http://www.kxdaili.com/dailiip.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35'
    }
    response = requests.get(url=url, headers=headers)
    with open(r'C:\Users\duanjiatao\Desktop\xxx.html', 'w', encoding=response.encoding) as file:
        file.write(response.text)
