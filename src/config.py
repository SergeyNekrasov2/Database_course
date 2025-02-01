from configparser import ConfigParser


# def config(filename="database.ini", section="postgresql"):
#     """Функция для получения словаря с данными для подключения к БД"""
#     # create a parser
#     parser = ConfigParser()
#     # read config file
#     parser.read(filename)
#     db = {}
#     if parser.has_section(section):
#         params = parser.items(section)
#         for param in params:
#             db[param[0]] = param[1]
#     else:
#         raise Exception(
#             'Section {0} is not found in the {1} file.'.format(section, filename))
#     return db


def config(filename=r'/database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    # получить раздел, по умолчанию postgresql
    db = {}

    if parser.has_section(section):
        print(section)
        params = parser.items(section)

        for param in params:
            db[param[0]] = param[1]
        else:
            raise Exception("Раздел {0} не найдено в {1} файл".format(section, filename))
    return db
