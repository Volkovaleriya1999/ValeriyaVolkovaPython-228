from model import ArticleModel


def add_title(msg):
    def inner_decorator(func):
        def wrapper(*args, **kwargs):
            print(msg.center(50, '='))
            result = func(*args, **kwargs)
            print('=' * 50, '\n')
            return result
        return wrapper
    return inner_decorator


class UserInterface:
    @add_title(' Ввод пользовательских данных. ')
    def wait_user_answer(self):
        print('Действия со статьями:')
        print('1 - создание статьи')
        print('\n2 - просмотр статей')
        print('\n3 - просмотр определенной статьи')
        print('\n4 - удаление статьи')
        print('\nq - выход из программы')
        user_answer = input('Выберите вариант действия: ')
        return user_answer

    @add_title(' Создание статьи. ')
    def add_user_article(self):

        dict_article = {
            'название': None,
            'автор': None,
            'количество страниц': None,
            'описание': None
        }

        for key in dict_article:
            dict_article[key] = input(f'Введите {key} статьи: ')
        return dict_article


    @add_title(' Список статей: ')
    def show_all_articles(self, articles):
        for ind, article in enumerate(articles, start=1):
            print(f'{ind}. {article}')