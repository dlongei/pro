import requests

url = 'http://122.224.91.58:9501/Frame/'

data = {'pvId': '376','jumpIndex':0}

response = requests.get(url=url, params=data)

res = response.text

print(res)