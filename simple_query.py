# -*- coding: utf-8 -*-
import pypyodbc as p


def simple_query(sql):
    con_str = 'Driver={SQL Server};' \
              'Server=192.168.11.9 ;' \
              'Database=i_collect;' \
              'Uid=sa;Pwd=12121212;'
    con = p.connect(con_str, autocommit=True)
    cur = con.cursor()
    r = cur.execute(sql)
    for i in r:
        print i
