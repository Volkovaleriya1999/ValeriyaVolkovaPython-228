from bs4 import BeautifulSoup
import requests
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('games.csv', 'a', encoding='utf-8-sig') as f:
        writer = csv.writer(f, lineterminator='\r', delimiter=';')
        writer.writerow((data['name'],
                         data['author'],
                         data['snippet'],
                         data['date'],
                         data['url']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    elements = soup.find_all('section', class_='_card__bottom_8sstg_1')
    for element in elements:

        try:
            name = element.find('a', class_='_card__title_8sstg_1 _card__title--has-subtitle_8sstg_1').text.strip()
        except ValueError:
            name = ''
        except AttributeError:
            name = ''

        try:
            author = element.find('a').text.strip()
        except ValueError:
            author = ''

        try:
            snippet = element.find('span', class_='_card__subtitle_8sstg_1').text
        except ValueError:
            snippet = ''
        except AttributeError:
            snippet = ''

        try:
            date = element.find('section', class_='_card__date_8sstg_1').text.strip()
        except ValueError:
            date = ''

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
            'date': date
        }
        write_csv(data)


def main():
    for i in range(1, 27):
        url = f'https://stopgame.ru/review/p{i}?subsection=izumitelno'
        get_data(get_html(url))


if __name__ == '__main__':
    main()

