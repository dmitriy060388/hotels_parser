import psycopg2
from psycopg2 import sql

DBNAME='mts_test_1'
DBUSER='postgres'
DBPASSWORD='P@ssw0rd!'
DBHOST='localhost'
DBPORT='5432'

conn = psycopg2.connect(dbname=DBNAME, user=DBUSER, password=DBPASSWORD, host=DBHOST, port=DBPORT)
conn.autocommit = True

#def psconnect(psdbname, psuser, pspasswrd, pshost, psport)
#def psclose()
#def psinsert(dbcon, id, hotel_name, date, price, category, breakfast)

logging = "ERROR" # состояния: ERROR, DEBUG. В состоянии DEBUG в терминал будет попадать вывод из postgres


def check_scheme_existence(dbcon, scheme_name, logdb):
    exists = False
    try:
        cur = dbcon.cursor()
        cur.execute(
            sql.SQL("select exists (select * from {})")
            .format(sql.Identifier(scheme_name)))
        if cur.fetchone()[0] > 0: #схема существует
            if logdb == "DEBUG":
                cur.fetchone()[0]
                print ("scheme %s exists" %scheme_name)
        else: #схема отсутствует
            if logdb == "DEBUG":
                cur.fetchone()[0]
                print ("scheme %s must be created" %scheme_name)
                create_scheme(dbcon, scheme_name, DBUSER, logging)
        cur.close()
        dbcon.close()
    except psycopg2.Error as e:
        if logdb == "DEBUG":
            print (e)
        #print("log [info]: error checking the existence of scheme %s!" %scheme_name)
    return exists

def check_table_existence(dbcon, scheme_name, table_name, logdb):
    exists = False
    try:
        cur = dbcon.cursor()
        cur.execute(
            sql.SQL("select exists (select * from {} where table_name=%s)")
            .format(sql.Identifier(scheme_name), (table_name)))
        if logdb == "DEBUG":
            cur.fetchone()[0]
        print ("log [info]: table %s in scheme %s exists" %(table_name, scheme_name))
        cur.close()
        dbcon.close()
    except psycopg2.Error as e:
        if logdb == "DEBUG":
            print (e)
        print("log [info]: table %s in scheme %s not exists!" %(table_name, scheme_name))
    return exists

def create_scheme(dbcon, create_scheme_name, create_scheme_admin, logdb):
    try:
        cur = dbcon.cursor()
        cur.execute(
            sql.SQL("create schema if not exists {scheme} AUTHORIZATION {login};").format(
                scheme=sql.Identifier(create_scheme_name),
                login=sql.Identifier(create_scheme_admin)))
        if logdb == "DEBUG":
            cur.fetchone()[0]
        print ("log [info]: scheme %s created" %create_scheme_name)
        print ("log [info]: scheme admin is %s" %create_scheme_admin)
        cur.close()
        dbcon.close()
    except psycopg2.Error as e:   
        if logdb == "DEBUG":     
            print (e)
        print("log [error]: error creating scheme %s!" %create_scheme_name)
    return

check_scheme_existence(conn, "mts_scheme", logging)
check_table_existence(conn, "mts_scheme", "result", logging)

