import psycopg2

try:
    # подключение к БД
    conn = psycopg2.connect(dbname='mts_test_1', user='postgres', password='P@ssw0rd!', host='localhost', port='5432')
    conn.autocommit = True
    print('yeah1')
except:
    # вывод ошибки при невозможности подключения к БД
    print('Can`t establish connection to database')

# работа с БД, предполагается, что уже создана схема mts_test_1 внутри бд mts_test_1 с доступом от учетки mtsadmin
cursor = conn.cursor()
#cursor.execute("DROP TABLE mts_test_1.results CASCADE")
#cursor.execute("CREATE TABLE mts_test_1.results (id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY, hotel_name VARCHAR(200), date DATE, price INT, category VARCHAR(128), breakfast BOOLEAN);")
#cursor.fetchone()
print('yeah2')
#норм cursor.execute("INSERT INTO mts_test_1.results (id, hotel_name, date, price, category, breakfast) VALUES (%s, %s, %s, %s, %s, %s);",(1,"pavelyaga", 1/1/2023, 1610, "standard", 1))
#норм cursor.fetchone()
cursor.close()
conn.close()