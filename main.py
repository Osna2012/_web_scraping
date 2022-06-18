import requests
import bs4

url = 'https://habr.com'

HEADERS = {'authority': 'assets.habr.com',
'method': 'GET',
'path': '/habr-web/css/page-company~page-flow~page-hub~page-user.235452ab.css',
'scheme': 'https',
'accept': 'text/css,*/*;q=0.1',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7',
'cookie': '_ga=GA1.2.1174349989.1652390103; _ym_d=1652390103; _ym_uid=1652390103727618464; _ym_isad=2; _gid=GA1.2.528563207.1655564702; _gat_gtag_UA_726094_1=1',
'referer': 'https://habr.com/ru/all/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'style',
'sec-fetch-mode': 'no-cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

DESIRED_HUBS = ['дизайн', 'нейросеть', 'mysql', 'python']

response = requests.get(url, headers=HEADERS)
#response.raise_for_status()

text = response.text
#print(text)

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
#print(articles)
for article in articles:
      hubs = article.find(class_="tm-article-snippet__title-link")
      hubs = set(hub.text.strip() for hub in hubs)
      # print(hubs)
      for hub in hubs:
            for word in DESIRED_HUBS:
                  if word in hub.lower():
                        href = article.find(class_='tm-article-snippet__title-link').attrs['href']
                        #print(url+href)
                        title = article.find('h2').find('span').text
                        #print(title)
                        data = article.find("time").attrs['title'].split(',')
                        #print(data[0])
                        print(f'{data[0]} - {title} - {url+href}')

