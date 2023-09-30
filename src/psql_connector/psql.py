import psycopg2

try:
    # подключение к БД
    conn = psycopg2.connect(dbname='mts_test_1', user='postgres', password='P@ssw0rd!', host='localhost')
except:
    # вывод ошибки при невозможности подключения к БД
    print('Can`t establish connection to database')
cursor = conn.cursor()
