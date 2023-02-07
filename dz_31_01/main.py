import json
dict_country = {}

class DictOfCountry:
    def __init__(self, country, capital):
        self.country = country
        self.capital = capital
        dict_country = {
            self.country: self.capital
        }

    def append_data(self, key, value):
        dict_country[key] = value

    def delete_data(self, key):
        try:
            del dict_country[key]
        except KeyError:
            print('Такой страны нет в словаре!')

    def search_data(self, key):
        print(dict_country.get(key, 'Такой страны нет в словаре!'))

    def editing_data(self, key, value):
        dict_country[key] = value

    def look_data(self):
        for key, value in dict_country.items():
            print(f'Страна: {key}\nСтолица: {value}\n')

    @staticmethod
    def dump_countries(file, dict):
        try:
            data = json.load(open(file))
        except FileNotFoundError:
            data = []

        with open(file, 'w') as f:
            for key, value in dict.items():
                data.append([key, value])
            json.dump(data, f, indent=2)

    @staticmethod
    def upload_countries(file):
        with open(file, 'r') as f:
                print(json.load(f))



answer = ''

while answer != '6':

    answer = input('Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n4 - редактирование '
                   'данных\n5 - просмотр данных\n6 - завершение работы\n')
    if answer == '1':
        country = input('Введите страну: ').title()
        capital = input('Введите столицу: ').title()
        my_dict = DictOfCountry(country, capital)
        my_dict.append_data(country, capital)
        DictOfCountry.dump_countries('countries.json', dict_country)

    elif answer == '2':
        country = input('Введите страну, которую хотите удалить: ').title()
        my_dict.delete_data(country)

    elif answer == '3':
        country = input('Введите страну, которую хотите найти: ').title()
        my_dict.search_data(country)

    elif answer == '4':
        country = input('Введите страну, которую хотите отредактировать: ').title()
        if country in dict_country:
            capital = input('Введите новую столицу для этой страны: ').title()
            my_dict.editing_data(country, capital)
        else:
            print('Такой страны нет в словаре!')

    elif answer == '5':
        my_dict.look_data()
        DictOfCountry.upload_countries('countries.json')
    else:
        print('Такого действия нет в меню.')








