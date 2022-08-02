import requests
from bs4 import BeautifulSoup
from pprint import pprint

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
HEADERS = {'Cookie': '_ym_d=1652015864; _ym_uid=165201586498419288; fl=ru; hl=ru; _ga=GA1.2.1927791662.1652015865; habr_web_home_feed=/all/; visited_articles=483400; _ym_isad=2; _gid=GA1.2.302197860.1659462176',
        'Host': 'habr.com',
        'Referer': 'https://github.com/netology-code/py-homeworks-advanced/tree/master/6.Web-scrapping',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
text =response.text

result = []
soup = BeautifulSoup(text, features="html.parser")
articles = soup.find_all(class_="tm-articles-list__item")
for article in articles:
    preview = article.find(class_="tm-article-body tm-article-snippet__lead").text
    for word in KEYWORDS:
        if word in preview:
            heading = article.find('h2')
            data = article.find('time')
            href = heading.find('a').attrs['href']
            url = 'https://habr.com' + href
            # print (f'{data.text} : {heading.text} --> {url}')
            result.append([data.text, heading.text, url])
pprint (result)