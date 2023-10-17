import psycopg2
from psycopg2 import sql
from pages.hotel_page.psql_connect import (DBNAME,
                                           DBUSER,
                                           DBPASSWORD,
                                           DBHOST,
                                           DBPORT)

conn = psycopg2.connect(
     dbname=DBNAME,
     user=DBUSER,
     password=DBPASSWORD,
     host=DBHOST,
     port=DBPORT)
conn.autocommit = True


def scheme_init(dbcon, create_scheme_name, create_scheme_admin, logdb):
    try:
        cur = dbcon.cursor()
        # создание схемы при отсутствии
        cur.execute(
            sql.SQL(
                "create schema if not exists {scheme} AUTHORIZATION {login};"
                ).format(
                scheme=sql.Identifier(create_scheme_name),
                login=sql.Identifier(create_scheme_admin)))
        if logdb == "DEBUG":
            print(
                "scheme "
                '"%s"'
                " created or already here. Admin user is: "
                '"%s"'
                "" % (create_scheme_name, create_scheme_admin)
            )
    except psycopg2.Error as e:
        if logdb == "DEBUG":
            print(e)
    return


def table_init(dbcon, scheme_name, create_table_name, logdb):
    try:
        cur = dbcon.cursor()
        cur.execute(
            sql.SQL(
                "create table if not exists {scheme}.{table} "
                "(id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY, "
                "hotel_name VARCHAR(1000), date VARCHAR(1000), "
                "price VARCHAR(1000), "
                "category VARCHAR(1000), breakfast VARCHAR(1000));"
                ).format(
                scheme=sql.Identifier(scheme_name),
                table=sql.Identifier(create_table_name)))
        if logdb == "DEBUG":
            print(
                "table "
                '"%s"'
                " in scheme "
                '"%s"'
                " created or already here" % (create_table_name, scheme_name)
            )
    except psycopg2.Error as e:
        if logdb == "DEBUG":
            print(e)
    return


def table_insert(
        dbcon,
        scheme_name,
        table_name,
        hotel_name,
        hotel_date,
        price,
        category,
        eat,
        logdb):
    try:
        if hotel_date is None:
            hotel_date = "date not found"
        if price is None:
            price = "price not found"
        if category is None:
            category = "категория номера не найдена"
        if eat is None:
            eat = "breakfast condition not found"
        if hotel_name is None:
            hotel_name = "hotel not found"
        cur = dbcon.cursor()
        cur.execute(
            sql.SQL(
                "insert into {scheme}.{table} "
                "(hotel_name, date, price, category, breakfast) "
                "overriding system value values (%s, %s, %s, %s, %s);"
                ).format(
                scheme=sql.Identifier(scheme_name),
                table=sql.Identifier(table_name)), (
                    hotel_name,
                    hotel_date,
                    price,
                    category,
                    eat))
    except psycopg2.Error as e:
        if logdb == "DEBUG":
            print(e)
    return
