import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(dbname='mts_test_1', user='postgres', password='P@ssw0rd!', host='localhost', port='5432')
conn.autocommit = True

#def psconnect(psdbname, psuser, pspasswrd, pshost, psport)
#def psclose()
#def check_existence_and_or_create
#def psinsert(dbcon, id, hotel_name, date, price, category, breakfast)


def check_existence(dbcon, scheme_name, table_str):
#    table_str = "results"
    exists = False
    try:
        cur = dbcon.cursor()
        cur.execute(
            sql.SQL("select exists (select * from {} where table_name=%s)")
            .format(sql.Identifier(scheme_name), (table_str)))
#1        psqlexec = "select exists(select * from mts_test1.mts_scheme where table_name= %s)"
#1        psqldata = (table_str,)
#       cur.execute("select exists(select * from mts_scheme where table_name=%s)", (table_str,))
#2        cur.execute("select exists(select * from %s where table_name= %s)", (scheme_name, table_str,))
#1        cur.execute(psqlexec, psqldata)
        cur.fetchone()[0]
        print ("exists")
        cur.close()
        dbcon.close()
    except psycopg2.Error as e:
        print (e)
    return exists

check_existence(conn, "mts_test1.mts_scheme", "result")
#def table_exists(conn, "results")
