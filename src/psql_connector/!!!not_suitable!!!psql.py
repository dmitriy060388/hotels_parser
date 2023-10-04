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



#table_insert(conn, "mts_scheme", "result", '3', 'pavelyaga', '2023-12-31', '1200', 'standard', '1', LOGGING)

def table_insert(dbcon, scheme_name, table_name, dbid, hotel_name, hotel_date, price, category, eat, logdb):
    try:
        cur = dbcon.cursor()
        cur.execute(
            sql.SQL("insert into {scheme}.{table} (id, hotel_name, date, price, category, breakfast) VALUES ({id}, {hname}, {date}, {price}, {category}, {eat});").format(
            scheme=sql.Identifier(scheme_name),
            table=sql.Identifier(table_name),
            id=sql.Identifier(dbid),
            hname=sql.Identifier(hotel_name),
            date=sql.Identifier(hotel_date),
            price=sql.Identifier(price),
            category=sql.Identifier(category),
            eat=sql.Identifier(eat)))
    except psycopg2.Error as e:
            if logdb == "DEBUG":
                print (e)
    return


#scheme_init(conn, "mts_scheme", DBUSER, LOGGING)
#table_init(conn, "mts_scheme", "result", LOGGING)
#table_insert(conn, "mts_scheme", "result", '1', 'pavelyaga', '2023-12-31', '1200', 'standard', '1', LOGGING)
#table_insert(conn, "mts_scheme", "result", '2', 'pavelyaga', '2023-12-31', '1200', 'standard', '1', LOGGING)