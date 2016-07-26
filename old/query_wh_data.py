# -*- coding: utf-8 -*-
import pypyodbc as p

class QueryWhData(object):

    """SQL Query from Database: wh_data"""

    #TODO реализовать хранилище данных с типом продукта
    product = '''
    blah blah blah
    '''

    def __init__(self, sql):
        self.con_str = 'Driver={SQL Server};' \
                       'Server=192.168.11.9 ;' \
                       'Database=wh_data;' \
                       'Uid=sa;Pwd=12121212;'
        self.con = p.connect(self.con_str, autocommit=True)
        self.cur = self.con.cursor()
        self.r = self.cur.execute(sql)
        self.column_list = [tuple[0] for tuple in self.r.description]
        self.res = self.r.fetchall()

    @property
    def one(self):
        print self.column_list[0]
        for i in self.res:
            print i[0]
        self.cur.close()

    @property
    def two(self):
        print self.column_list[0], ' ', self.column_list[1]
        for i in self.res:
            print i[0], ' ', i[1]
        self.cur.close()