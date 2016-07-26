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

    def __init__(self):
        self.con_str = 'Driver={SQL Server};' \
                       'Server=192.168.11.9 ;' \
                       'Database=i_collect;' \
                       'Uid=sa;Pwd=12121212;'
        self.connection = None

    def connect(self):
        if not self.connection:
            self.connection = p.connect(self.con_str, autocommit=True)

    def _make_query(self, sql_query):
        if not self.connection:
            print "not connected to DB"
            return
        cur = self.connection.cursor()
        res = cur.execute(sql_query)
        cur.close()
        return res

    @staticmethod
    def _get_column_list_from_res(res):
        return [tpl[0] for tpl in res.description]

    def one(self, sql_query):
        res = self._make_query(sql_query)
        print self._get_column_list_from_res(res)[0]
        for i in res:
            print i[0]

    def two(self, sql_query):
        res = self._make_query(sql_query)
        column_list = self._get_column_list_from_res(res)
        print column_list[0], ' ', column_list[1]
        for i in res:
            print i[0], ' ', i[1]

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None