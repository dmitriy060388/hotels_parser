import psycopg2

try:
    # подключение к БД
    conn = psycopg2.connect(dbname='mts_test_1', user='postgres', password='P@ssw0rd!', host='localhost', port='5432')
    print('yeah1')
except:
    # вывод ошибки при невозможности подключения к БД
    print('Can`t establish connection to database')

# работа с БД, предполагается, что уже создан экземпляр mts_test_1 с доступом от учетки mtsadmin
cursor = conn.cursor()
cursor.execute("CREATE TABLE mts_test_1.results (id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY, hotel_name VARCHAR(200), date DATE, price INT, category VARCHAR(128), breakfast BOOLEAN);")
print('yeah2')
conn.close()
