# -*- coding: utf-8 -*-
import pypyodbc as p


bank = u'''
    SELECT DISTINCT
        b.id
        ,N''+ b.name as name
    FROM
        i_collect.dbo.bank as b
        inner join i_collect.dbo.portfolio as p on b.id = p.parent_id
    WHERE
        p.status = 2
    ORDER BY
        N'' + b.name asc
    '''
portfolio = u'''
    SELECT DISTINCT
        p.id
        ,N''+ p.name as name
    FROM
        i_collect.dbo.portfolio p
    WHERE
        p.status = 2
        and p.parent_id {}
    ORDER BY
        N'' + p.name asc
    '''

phone_typ = u'''
    select
        di.code
        ,N''+ di.name name
    from
        i_collect.dbo.dict di
    where
        parent_id = 4'''


class QueryICollect(object):

    """SQL Query from Database: i_collect"""

    def __init__(self, sql):
        self.con_str = 'Driver={SQL Server};' \
                       'Server=192.168.11.9 ;' \
                       'Database=i_collect;' \
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