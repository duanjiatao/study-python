"""
测试数据库连接池
"""

import pymysql
from dbutils.pooled_db import PooledDB

from .config import get_mysql_connect_conf
from .config import get_mysql_pool_conf

POOL = PooledDB(
    creator=pymysql,  # 使用 PyMySQL 作为连接器
    # maxconnections=5,  # 连接池最大连接数
    # mincached=2,  # 初始化时建立的连接数
    # maxcached=5,  # 连接池最大缓存数量
    # maxshared=3,  # 连接池最大共享数量
    # blocking=True,  # 是否阻塞等待
    **get_mysql_pool_conf(),  # 连接池信息
    **get_mysql_connect_conf()  # 数据库连接信息
)


def get_conn():
    conn = POOL.connection()
    cursor = conn.cursor()
    return conn, cursor


def close(conn, cursor):
    cursor.close()
    conn.close()


def insert(name, sex, age):
    conn, cursor = get_conn()
    sql = "INSERT INTO student (name, sex, age, create_time, update_time) VALUES (%s, %s, %s, sysdate(), sysdate())"
    try:
        cursor.execute(sql, (name, sex, age))
        conn.commit()
        print("插入成功")
    except Exception as e:
        print("插入失败: ", e)
        conn.rollback()
    finally:
        close(conn, cursor)


def test1():
    print("PooledDB 连接池信息:", POOL.__dict__)
    conn, cursor = get_conn()
    cursor.execute('select * from student')
    rows = cursor.fetchone()
    print(rows)
    close(conn, cursor)


def test_insert():
    insert('张三', '1', '22')
