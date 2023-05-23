import json

import requests

url = "https://fanyi.baidu.com/v2transapi"

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Acs-Token': '1679534957948_1679535138031_L5DaoBST95vfrj++gIccRwu9avElbLGWAW1y7ytmzqBdNJFv1tYVUgSvvpUBszsMo/eiwGF7V/u3z2HOGaahNC5CYG2489NdjtMAC0LtY3+/mOO6kz5wRL9edvCzMZVwlDWqpqEY8GY0d0AQPuiWMsL/U/8ZPMD7b24VgopR9/JmpkPQiX4E0V7MIgG+4oDSojP/wppMsU/7CV3UsM6/mDRtjYBJVJCjY6OneXf3weXFHaN0vesT6xR69RUK914MoGOarA+eaWMKTCRx/sneZm7zIwoH5VM40d8S8x/XaDYoYW9bSFYHZ5W+hBN/QctAQjnf8yatQEdLTn/8b/Hxvj9EDKKOKg2ldU+i+EExZQdZh9oZNuuefFgoK9JlMi81',
    'Connection': 'keep-alive',
    'Content-Length': '150',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=7ED10987871A49680B7B2D19E1A8215A; PSTM=1584070553; BDUSS=DlqNEp1UWFWLWJ-ZWZ0QTZEc1RIMmtnUlJqakcyc0dSNWd3YlR6V1dad1ZBRXRmSUFBQUFBJCQAAAAAAAAAAAEAAADCjt0xxOO0877LOTkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABVzI18VcyNfW; BDUSS_BFESS=DlqNEp1UWFWLWJ-ZWZ0QTZEc1RIMmtnUlJqakcyc0dSNWd3YlR6V1dad1ZBRXRmSUFBQUFBJCQAAAAAAAAAAAEAAADCjt0xxOO0877LOTkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABVzI18VcyNfW; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; __yjs_duid=1_c9a41b9e4819aae090592c983eae48051620269154294; BAIDUID=4785DB06EE87D615D08D7FF9C2DD0AB5:FG=1; MCITY=-%3A; APPGUIDE_10_0_2=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BA_HECTOR=81ag0l2l2hah0504a0008gf71i1lp9i1n; delPer=0; PSINO=6; ZFY=ujj7cxJ4BQWp7ioAEyjoUx14WC9qXNucp1ACblfmwCM:C; BAIDUID_BFESS=4785DB06EE87D615D08D7FF9C2DD0AB5:FG=1; BDRCVFR[4Zjqyl1bxbt]=aeXf-1x8UdYcs; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1678952860,1679486180; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1679486500; H_PS_PSSID=38185_36543_38407_38354_38366_38307_37861_38170_38290_38379_38434_38262_37938_38315_38382_37900_26350_38282_37881; ab_sr=1.0.1_Mjg0Mjc1NzM4MDUwZjQyMTgzNDUwOTg4MmI5ZDNlMmUzZTlkMDQyOWZmMzdlYTE3ZmZkNTg5YjczMjI4MTRiOWI3NDJmMzQxYzNmOWI1YmE5NWFhMTkzODU2MThjZjI0YzRmYmU4MWNhMDZmMWY3NTliODFlY2IwZmE0ZThlM2M2ZTEyNTI5Yjc1MDAxNGFkMmQyZWEzYWI3NWU0ODQ0OWJmMTM2MmE0ZGY1YzJjYTBlODVhMzZlYzUzZTVhMzg5',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/translate?aldtype=16047&query=%E6%95%B0%E5%AD%A6&keyfrom=baidu&smartresult=dict&lang=auto2zh',
    'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.43',
    'X-Requested-With': 'XMLHttpRequest'
}

data_dict = {
    "query": "数学",
    "from": "zh",
    "to": "en",
    "transtype": "translang",
    "simple_means_flag": "3",
    "sign": "636725.873476",
    "token": "33cc5f57d733ab72847fd7ab936003a3",
    "domain": "common"
}

response = requests.post(url, data=data_dict)
# print(response.text)
# print(response.status_code)
print(json.dumps(json.loads(response.text), indent=4, ensure_ascii=False))
