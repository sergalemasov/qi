# -*- coding: utf-8 -*-
import pypyodbc as p


class ExecQueryICollect(object):
    """Just exec some Query from db: i_collect"""

    def __init__(self):
        self.con_str = 'Driver={SQL Server};' \
                       'Server=192.168.11.9 ;' \
                       'Database=i_collect;' \
                       'Uid=sa;Pwd=12121212;'
        self.con = p.connect(self.con_str, autocommit=True)
        self.cur = self.con.cursor()

    def i_collect_exec(self, sql):
        self.cur.execute(sql)
        self.cur.close()


class ExecQueryWhData(object):
    """Just exec some Query from db: wh_data"""

    def __init__(self):
        self.con_str = 'Driver={SQL Server};' \
                       'Server=192.168.11.9 ;' \
                       'Database=wh_data;' \
                       'Uid=sa;Pwd=12121212;'
        self.con = p.connect(self.con_str, autocommit=True)
        self.cur = self.con.cursor()

    def wh_data_exec(self, sql):
        self.cur.execute(sql)
        self.cur.close()
