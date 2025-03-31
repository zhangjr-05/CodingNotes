import re
import requests
from tqdm import tqdm

url = 'https://leetcode.cn/problemset/all-code-essentials/?page='

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"}

bank = []

for i in tqdm(range(1, 2), '玩命爬取中...'):
    url = url + str(i)

    finished = False
    while not finished:
        try:
            response = requests.get(url, headers=headers)
            response.encoding = response.apparent_encoding
            html = response.text
            print(html)
            question = re.findall(r'class="h-5 hover:text-blue-s dark:hover:text-dark-blue-s">(.*?)</a>', html, re.S)
            bank.extend(question)
            finished = True
        except Exception as e:
            print(e, 'qwq')

print(bank)