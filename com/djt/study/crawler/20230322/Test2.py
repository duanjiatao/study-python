import json

import requests

url = 'https://mng-dev.jlpay.com/manage/dispatch/ruleexp?commandId=findBaseRuleRpc'

headers = {
    'platcode': 'risk',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.43',
    'cookie': 'experimentation_subject_id=IjFjY2Q2YzVjLTcwNWItNDA2OC04YWIwLTIzZDdjYTQ5N2M0MiI=--9ccaf4e2c4c9cbfa5d48c84e8d02ac0d2cf55b0c; jlpay_access_token=eyJ0eXAiOiJKV1QiLCJwbGF0IjoiQUMiLCJhbGciOiJTTTNXaXRoU00yIn0.eyJzdWIiOiJQIiwidWlkIjoiMjAyMDAyMTc4MDA0MTY0OCIsIm5iZiI6MTY3OTQ2Njg3NywidW5hbWUiOiLmrrXkvbPmtpsiLCJpc3MiOiJKTFBBWSIsImV4cCI6MTY3OTU1MzI3NywiaWF0IjoxNjc5NDY2ODc3LCJqdGkiOiIxOTEwNjMzMTI0MzM3Njc3MVJ2NjNlODJpNUgifQ.MEUCIQCGgIgL0atVLBd7QvKvbE-UDrEvW0tD-oqkZsEziK2UagIgDX74FIweG8Z6ZE73XCbukXBTzN7vrUeHo9yh_unKo8Y; MANAGE-FRONT-SESSION=061b87ba-5b33-41e2-8603-90d0588e607d'
}

params = {
    'ruleDesc': 'isTrue',
    'ruleType': '02'
}

response = requests.post(url=url, headers=headers, json=params)
# response.encoding = response.apparent_encoding
# print(response.text)
# 格式化json
print(json.dumps(json.loads(response.text), indent=4, ensure_ascii=False))

print("=" * 30)
url = 'https://www.baidu.com'
response = requests.get(url, timeout=1)
for k, v in response.cookies.items():
    print(f'{k}={v}')
