import requests
import re
from bs4 import BeautifulSoup
from tqdm import tqdm

url = 'https://www.bqgui.cc/book/491'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

book_info = soup.find('div', attrs={'class': 'info'})
book_title = book_info.find('h1').text
book_author = book_info.find('div', attrs={'class': 'small'}).find('span').text
book_latest_href = book_info.find('div', attrs={'class': 'small'}).find('a')['href']
book_latest_num = int(re.findall(r'\d+', book_latest_href)[1])

with open('d:/mypython/Web_Crawler/crawler_library/小说/庆余年', 'a', encoding='utf-8') as f:
    for i in tqdm(range(1, book_latest_num + 1), desc=f'{book_title}  {book_author}  正在爬取'):
        chapter_url = 'https://www.bi02.cc/kan/45731/' + f'{i}.html'
        chapter_response = requests.get(chapter_url, headers=headers)
        chapter_soup = BeautifulSoup(chapter_response.text, 'html.parser')
        chapter_title = chapter_soup.find('div', attrs={'class': 'content'}).find('h1').text
        chapter_content = chapter_soup.find('div', attrs={'id': 'chaptercontent'}).text
        index = chapter_content.rfind('请收藏本站')
        f.write(chapter_title + '\n')
        f.write(chapter_content[0:index].replace('　　', '\n') + '\n')
                