import psycopg2

conn = psycopg2.connect(dbname='mts_test_1', user='postgres', password='P@ssw0rd!', host='localhost', port='5432')
conn.autocommit = True

#def psconnect(psdbname, psuser, pspasswrd, pshost, psport)
#def psclose()
#def check_existence_and_or_create
#def psinsert(dbcon, id, hotel_name, date, price, category, breakfast)


def check_existence(dbcon, table_str):
#    table_str = "results"
    exists = False
    try:
        cur = dbcon.cursor()
        psqlexec = "select exists(select * from mts_test1.mts_scheme where table_name= %s)"
        psqldata = (table_str,)
#       cur.execute("select exists(select * from mts_scheme where table_name=%s)", (table_str,))
#        cur.execute("select exists(select * from %s where table_name= %s)", (schema_name, table_str,))
        cur.execute(psqlexec, psqldata)
        cur.fetchone()[0]
        print ("exists")
        cur.close()
        dbcon.close()
    except psycopg2.Error as e:
        print (e)
    return exists

check_existence(conn, "result")
#def table_exists(conn, "results")
