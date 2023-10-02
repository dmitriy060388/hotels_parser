import psycopg2


try:
    # подключение к БД
    conn = psycopg2.connect(dbname='mts_test_1', user='postgres', password='P@ssw0rd!', host='localhost', port='5432')
    conn.autocommit = True
    print('yeah1')
except:
    # вывод ошибки при невозможности подключения к БД
    print('Can`t establish connection to database')