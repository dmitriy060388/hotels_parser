import psycopg2

conn = psycopg2.connect(dbname='mts_test_1', user='postgres', password='P@ssw0rd!', host='localhost', port='5432')
conn.autocommit = True

#def psconnect(psdbname, psuser, pspasswrd, pshost, psport)
#def psclose()
#def check_existence_and_or_create
#def psinsert(dbcon, id, hotel_name, date, price, category, breakfast)


def check_existence(dbcon, schema_name, table_str):
#    table_str = "results"
    exists = False
    try:
        cur = dbcon.cursor()
        cur.execute("select exists(select * from mts_scheme where table_name=%s)", (table_str,))
        cur.fetchone()[0]
        print ("exists")
        cur.close()
        dbcon.close()
    except psycopg2.Error as e:
        print (e)
    return exists

table_exists(conn, "results")