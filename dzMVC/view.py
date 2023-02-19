def add_title(msg):
    def inner_decorator(func):
        def wrapper(*args, **kwargs):
            print(msg.center(50, '*'))
            result = func(*args, **kwargs)
            print('*' * 50, '\n')
            return result
        return wrapper
    return inner_decorator


class UserInterface:
    @add_title(' Ввод пользовательских данных. ')
    def wait_user_answer(self):
        print('Действия с фильмами:')
        print('1 - добвление фильма')
        print('\n2 - каталог фильмов')
        print('\n3 - просмотр определенного фильма')
        print('\n4 - удаление фильма')
        print('\nq - выход из программы')
        user_answer = input('Выберите вариант действия: ')
        return user_answer


    @add_title(' Добавление фильма. ')
    def add_user_film(self):
        dict_film = {
            'название': None,
            'жанр': None,
            'режиссер': None,
            'год выпуска': None,
            'длительность': None,
            'студия': None,
            'актеры': None
        }

        for key in dict_film:
            dict_film[key] = input(f'Введите {key} фильма:')
        return dict_film


    @add_title(' Каталог фильмов. ')
    def show_all_films(self, films):
        for ind, film in enumerate(films, start=1):
            print(f'{ind}. {film}')


    @add_title(' Ввод названия. ')
    def get_user_film(self):
        user_film = input('Введите название фильма: ')
        return user_film


    @add_title(' Просмотр фильма: ')
    def show_single_film(self, film):
        for key in film:
            print(f'{key} фильма - {film[key]}')


    @add_title(' Сообщение об ошибке. ')
    def show_incorrect_title_error(self, user_title):
        print(f'Фильма с названием "{user_title}" не существует.')


    @add_title(' Сообщение об ошибке. ')
    def show_incorrect_answer_error(self, answer):
        print(f'Варианта "{answer}" не существует.')


    @add_title(' Удаление фильма. ')
    def remove_single_film(self, film):
        print(f'Фильм "{film}" успешно удален.')

