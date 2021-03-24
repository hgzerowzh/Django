import pymysql

def get_list(sql, args):
    conn = pymysql.connect(host='10.0.0.204', user='hgzero', port=3306, password='woshiniba', db='my_test', charset='utf8')
    conn_cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    conn_cursor.execute(sql, args)
    result = conn_cursor.fetchall()
    conn_cursor.close()
    conn.close()
    return result


def get_one(sql, args):
    conn = pymysql.connect(host='10.0.0.204', user='hgzero', port=3306, password='woshiniba', db='my_test', charset='utf8')
    conn_cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    conn_cursor.execute(sql, args)
    result = conn_cursor.fetchone()
    conn_cursor.close()
    conn.close()
    return result


def modify(sql, args):
    conn = pymysql.connect(host='10.0.0.204', user='hgzero', port=3306, password='woshiniba', db='my_test', charset='utf8')
    conn_cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    conn_cursor.execute(sql, args)
    conn.commit()
    conn_cursor.close()
    conn.close()

import pymysql
class SqlHelper(object):
    def __init__(self):
        self.connect()

    def connect(self):
        self.conn = pymysql.connect(host='10.0.0.204', user='hgzero', port=3306, password='woshiniba', db='my_test', charset='utf8')
        self.conn_cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def get_list(self, sql, args):
        self.conn_cursor.execute(sql, args)
        result = self.conn_cursor.fetchall()
        return result

    def get_one(self, sql, args):
        self.conn_cursor.execute(sql, args)
        result = self.conn_cursor.fetchone()
        return result

    def modify(self, sql, args):
        self.conn_cursor.execute(sql, args)
        self.conn.commit()

    # 这传入的args是列表，执行多条sql语句
    def multiple_modify(self, sql, args):
        # 语法示例：self.conn_cursor.execuremany('insert into students(name,age) values(%s,%s)', [(1, 'stu1'),(2, 'stu2')])
        self.conn_cursor.executemany(sql, args)
        self.conn.commit()

    def create(self, sql, args):
        self.conn_cursor.execute(sql, args)
        self.conn.commit()
        return self.conn_cursor.lastrowid  # 拿到最新的id值

    def close(self):
        self.conn_cursor.close()
        self.conn.close()

# 使用：
# obj = SqlHelper()
# obj.multiple_modify()
# obj.close()











