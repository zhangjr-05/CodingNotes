import requests


url = 'https://translate.google.com'

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"}

data = {}

response = requests.post(url, data=data)

print(response)

