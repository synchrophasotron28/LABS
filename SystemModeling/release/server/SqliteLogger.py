import sqlite3
import datetime


def get_create_table_query(table_name):
    query = "create table if not exists {}" \
            "(x REAL, y REAL, z REAL, theta REAL, " \
            " r REAL, p REAL, big_omega REAL, " \
            "omega REAL, e REAL, tau REAL, m REAL, i REAL );"
    return query.format(table_name)


def get_insert_query(key, x, y, z, theta, r1, p1, OMEGA1, omega1, e1, tau1, m, i1):
    query = f"""INSERT INTO {key} VALUES ({x},{y},{z},{theta},{r1},{p1},{OMEGA1},{omega1},{e1},{tau1},{m},{i1})"""
    return query


def get_unique_name():
    now = datetime.datetime.now()
    day = str(now.day).rjust(2, '0')
    month = str(now.month).rjust(2, '0')
    year = str(now.year)
    hour = str(now.hour).rjust(2, '0')
    minute = str(now.minute).rjust(2, '0')
    second = str(now.second).rjust(2, '0')
    result = f'{hour}{minute}{second}{day}{month}{year}.db'
    return result


def make_new_connection():
    database_name = get_unique_name()
    connection = sqlite3.connect()


print(get_create_table_query('test'))
