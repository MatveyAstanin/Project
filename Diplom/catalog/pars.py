from django.shortcuts import render
import asyncio
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup



picture = None
genre = None
platform = None
data = None
publisher = None
developer = None
screenshots = None
count = 0
countinfo = 0
san = []
url = 'https://gabestore.ru/publishers'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36', 'aceept': '*/*'}

async def quest():
    pass
response = requests.get(url, headers=HEADERS)
qoutes = BeautifulSoup(response.text, 'lxml')
soup = qoutes.find_all('a', class_='b-developer-card')
information = []
listscreenshots = []
for game in soup:
    resp = requests.get("https://gabestore.ru" + game.get('href'))
    qout = BeautifulSoup(resp.text, 'lxml')
    games = qout.find_all('div', class_='shop-item')
    for i in games:
        resp = requests.get("https://gabestore.ru" + i.find('a', class_='shop-item__name').get('href'))

        qoutt = BeautifulSoup(resp.text, 'lxml')
        count += 1
        title = i.find('a', class_='shop-item__name').text
        print(title)
        info = qoutt.find_all('div', class_='b-card__table-value')
        for text in info:
            countinfo += 1
            print(text.get_text())
            information.append(text.get_text())
            if countinfo > 4:
                break
        countinfo = 0
        genre = information[0]
        platform = information[1]
        data = information[2]
        publisher = information[3]
        developer = information[4]

        screenshots = qoutt.find_all('a', class_='js-fb')
        for screen in screenshots:
            listscreenshots.append(screen.get('href'))

        try:
            content = qoutt.find('div', class_='b-card__tabdescription').get_text()
            picture = qoutt.find('img', class_='js-img-bgcolro')['src']



        except:
            print("Error")
            content = None
            count -= 1
        finally:
            pass
        print(content)
        print(picture)
        print(genre)
        print(platform)
        print(data)
        print(publisher)
        print(developer)
        print(listscreenshots)
        price = i.find('div', class_='shop-item__price-current').text
        print(price)


    # model.title = i.find('a', class_='shop-item__name').text
    # model.content = qout.find('div', class_='b-card__tabdescription')
    # model.price = i.find('div', class_='shop-item__price-current').text
    # model.save()
    # info[title] = {price: content}
    # info[i.find('a', class_='shop-item__name').text] = i.find('a', class_='shop-item__name').get('href')
    # info[i.find('a', class_='shop-item__name').text][i.find('div', class_='shop-item__price-current').text] = \
    # i.find('a', class_='shop-item__name').get('href')
# for item in sas:
#     san.append((item.title + ": " + item.content).upper())
print(count)