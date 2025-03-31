import os
import re
import requests
from tqdm import tqdm

h_url = 'https://ssr1.scrape.center/page/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'}

pattern = r'class="m-b-sm">(.*?) .*?class="score m-t-md m-b-n-sm">.*?(\d.\d)</p>'

# 获取当前文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

finished = False
while not finished:
    try:
        with open(f'{current_dir}/text', 'w', encoding='utf-8') as f:

            for i in tqdm(range(1, 11), '爬取中......'):
                url = h_url + str(i)
                html = requests.get(url, headers=headers).text

                content = re.findall(pattern, html, re.DOTALL)
                for msg in content:

                    f.write(msg[0])
                    f.write(f"  评分: {msg[1]}\n")
        print('爬取成功ovo')
        finished = True
    except:
        print("发生意外qwq")