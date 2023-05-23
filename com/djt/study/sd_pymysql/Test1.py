"""
测试pymysql
"""
import pymysql

from .config import get_mysql_connect_conf


def get_conn():
    db_conf = get_mysql_connect_conf()
    conn = pymysql.connect(**db_conf)
    cursor = conn.cursor()
    return conn, cursor


def close(conn, cursor):
    cursor.close()
    conn.close()


def test1():
    print(f"PyMySQL 线程安全级别：{pymysql.threadsafety}")
    conn, cursor = get_conn()
    cursor.execute('select * from student')
    rows = cursor.fetchone()
    print(rows)
    close(conn, cursor)
