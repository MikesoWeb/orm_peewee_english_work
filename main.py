from peewee import *


class BaseModel(Model):
    class Meta:
        # Создание объекта базы данных
        database = SqliteDatabase(
            'demo_DB')


class English(BaseModel):
    id = PrimaryKeyField(null=False)
    word = CharField(max_length=100)
    translate = CharField(max_length=100)

    class Meta:
        db_table = 'english'


def insert_data():
    """Вставляем данные в таблицу с проверкой существования такого слова
    Если существует, выводим оповещение
    Если не существует, создаем запись"""

    word = input('Введите слово: ')
    if not English.select().where(English.word == word):
        translate = input('Введите перевод слова: ')
        English.create(word=word, translate=translate)


    else:
        print(f'Слово {word} уже существует!')
        print('')


def show_data():
    """Смотрим таблицу нашей базы данных"""

    for i in English.select().limit(5):
        print(i.id, i.word, i.translate)


def update_data():
    """Обновляем наши данные в таблице"""

    words = input('Введите для обновления: ')
    word_upd = input('На что обновить: ')
    # query = English.update(word=word_upd).where(English.word == words)
    query = English.update(translate=word_upd).where(English.word == words)
    query.execute()


def delete_data_table():
    """Удаляем данные из таблицы"""

    delete_data_query = input('Введите слово для удаления: ')
    del_word = English.select().where(English.word == delete_data_query)
    English.delete_by_id(del_word)


def main(query='None'):
    """Передаем запросы в функцию, получаем результат"""
    while True:
        if query != '':
            query = input('Введите q для выхода, i - вставка, s - просмотр таблицы, u - обновление, d - удаление: ')

            if query in ['q', 'й']:
                print('Программа завершена')
                break
            if query in ['d', 'в']:
                delete_data_table()
            if query in ['s', 'ы']:
                show_data()
            if query in ['i', 'ш']:
                insert_data()
            if query in ['u', 'г']:
                update_data()
        else:
            print('<неизвестный запрос>')


if __name__ == '__main__':
    English.create_table()
    main()
