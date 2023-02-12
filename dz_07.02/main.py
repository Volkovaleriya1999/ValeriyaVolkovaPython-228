from bs4 import BeautifulSoup
import requests
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('games.csv', 'a') as f:
        writer = csv.writer(f, lineterminator='\r', delimiter=';')
        writer.writerow((data['name'],
                         data['author'],
                         data['snippet'],
                         data['url']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    elements = soup.find_all('section', class_='_card__bottom_8sstg_1')
    for element in elements:

        try:
            name = element.find('a', class_='_card__title_8sstg_1 _card__title--has-subtitle_8sstg_1').text.strip()
        except ValueError:
            name = ''

        try:
            author = element.find('a').text.strip()
        except ValueError:
            author = ''

        try:
            snippet = element.find('span', class_='_card__subtitle_8sstg_1').text
        except ValueError:
            snippet = ''

        try:
            url = element.find('section', class_='_card__content_8sstg_390').find('a')['href']
            url1 = 'https://stopgame.ru' + url
        except ValueError:
            url1 = ''

        data = {
            'name': name,
            'author': author,
            'snippet': snippet,
            'url': url1,
        }
        write_csv(data)


def main():
    for i in range(1, 27):
        url = f'https://stopgame.ru/review/p{i}?subsection=izumitelno'
        get_data(get_html(url))


if __name__ == '__main__':
    main()