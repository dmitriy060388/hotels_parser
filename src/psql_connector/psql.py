import psycopg2
from psycopg2 import sql
from src.pages.hotel_page.psql_connect import DBNAME, DBUSER, DBPASSWORD, DBHOST, DBPORT, LOGGING

# DBNAME='mts_test_1'
# DBUSER='postgres'
# DBPASSWORD='P@ssw0rd!'
# DBHOST='localhost'
# DBPORT='5432'
# LOGGING = "DEBUG" # состояния: ERROR, DEBUG. В состоянии DEBUG в терминал будет попадать вывод из postgres

conn = psycopg2.connect(dbname=DBNAME, user=DBUSER, password=DBPASSWORD, host=DBHOST, port=DBPORT)
conn.autocommit = True

def scheme_init(dbcon, create_scheme_name, create_scheme_admin, logdb):
    try:
        cur = dbcon.cursor()
        #создание схемы при отсутствии
        cur.execute(
            sql.SQL("create schema if not exists {scheme} AUTHORIZATION {login};").format(
            scheme=sql.Identifier(create_scheme_name),
            login=sql.Identifier(create_scheme_admin)))
        if logdb == "DEBUG":
            print("scheme "'"%s"'" created or already here. Admin user is: "'"%s"'"" %(create_scheme_name, create_scheme_admin))
    except psycopg2.Error as e:
            if logdb == "DEBUG":
                print (e)
    return


def table_init(dbcon, scheme_name, create_table_name, logdb):
    try:
        cur = dbcon.cursor()
        cur.execute(
            sql.SQL("create table if not exists {scheme}.{table} (id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY, hotel_name VARCHAR(200), date DATE, price INT, category VARCHAR(128), breakfast BOOLEAN);").format(
            scheme=sql.Identifier(scheme_name),
            table=sql.Identifier(create_table_name)))
        if logdb == "DEBUG":
            print("table "'"%s"'" in scheme "'"%s"'" created or already here" %(create_table_name, scheme_name))
    except psycopg2.Error as e:
            if logdb == "DEBUG":
                print (e)
    return

def table_insert(dbcon, scheme_name, table_name, dbid, hotel_name, hotel_date, price, category, eat, logdb):
    try:
        cur = dbcon.cursor()
        cur.execute(
            sql.SQL("insert into {scheme}.{table} (id, hotel_name, date, price, category, breakfast) overriding system value values (%s, %s, %s, %s, %s, %s);").format(
            scheme=sql.Identifier(scheme_name),
            table=sql.Identifier(table_name)),(dbid, hotel_name, hotel_date, price, category, eat))
    except psycopg2.Error as e:
            if logdb == "DEBUG":
                print (e)
    return

def table_check_last_id(dbcon, scheme_name, table_name):
    try:
        cur = dbcon.cursor()
        cur.execute("select id from mts_scheme.result order by id desc limit 1")
        last_id = int(cur.fetchone()[0])
    except psycopg2.Error as e:
            if logdb == "DEBUG":
                print (e)
    return last_id


scheme_init(conn, "mts_scheme", DBUSER, LOGGING)
table_init(conn, "mts_scheme", "result", LOGGING)
maxid=table_check_last_id(conn, "mts_scheme", "result") + 1
table_insert(conn, "mts_scheme", "result", maxid, 'pavelyaga', '2023-12-31', '1200', 'standard', '1', LOGGING)


