import psycopg2


try:
    # подключение к БД
    conn = psycopg2.connect(dbname='mts_test_1', user='admcosmos', password='F9ut@R*_22M', host='localhost', port='5432')
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE mts_test_1.results (id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY, hotel_name VARCHAR(200), date DATE, price INT, category VARCHAR(128), breakfast BOOLEAN);")
    cursor.fetchall()
except:
    # вывод ошибки при невозможности подключения к БД
    print('Can`t establish connection to database')