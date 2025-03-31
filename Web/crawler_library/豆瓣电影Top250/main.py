import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

url = 'https://movie.douban.com/top250'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'}

finished = False
while not finished:
    try:
        with open('d:/mypython/Web_Crawler/crawler_library/豆瓣电影Top250/电影信息', 'w', encoding='utf-8') as f:
            
            for i in tqdm(range(0, 250, 25), desc='正在爬取'):
                response = requests.get(url + f'?start={i}&filter=', headers=headers)
                soup = BeautifulSoup(response.text, 'html.parser')

                all_titles = soup.findAll('span', attrs={'class': 'title'})
                all_titles = [title.text for title in all_titles if '/' not in title.text]

                all_stars = soup.findAll('span', attrs={'class': 'rating_num', 'property': 'v:average'})
                all_stars = [star.text for star in all_stars]

                for j in range(25):
                    f.write(f'{i + j + 1}  {all_titles[j]}  评分: {all_stars[j]}\n')

        finished = True
        print('爬取成功')
    except Exception as e:
        print(f'爬取失败：{e}')
        pass