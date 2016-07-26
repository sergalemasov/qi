# -*- coding: utf-8 -*-
from colorama import init
from termcolor import colored
from sql_queries import prom, mprom, calc, phone, perspect
init()


class FirstModuleList(object):
    """concatenate behavior part of SQL queries"""

    first_query = None

    def __init__(self):
        self.try_dict = {

            'prom': [prom, colored(u'даты регистрации и количество обещаний ', 'green'),
                     (colored(u'даты регистрации', 'magenta'),
                      colored(u'количество', 'magenta'))
            ]

            ,'mprom': [mprom,
                        colored(u'даты и количество пропущенных обещаний', 'green'),
                        (colored(u'даты', 'magenta'),
                         colored(u'количество', 'magenta'))
            ]

            ,'calc': [calc,
                       colored(u'даты оплат, суммы и количество', 'green'),
                       (colored(u'даты', 'magenta'),
                        colored(u'количество', 'magenta'),
                        colored(u'суммы', 'magenta'))
            ]

            , 'phone': [phone,
                        colored(u'тип телефона и статус', 'green'), (colored(u'''
1   Мобильный
2   Домашний
3   Рабочий
4   Дополнительный
41  Поручитель-Мобильный
42  Поручитель-Домашний
43  Поручитель-Рабочий
104 Поручитель-Дополнительный
201 Залогодатель-Мобильный
202 Залогодатель-Домашний
203 Залогодатель-Рабочий
204 Залогодатель-Дополнительный
31  Моб.Третье лицо
32  Дом.Третье лицо
33  Раб. Третье лицо
44  Суд Приставы
34  Доп. Третье лицо
205 Созаемщик-Мобильный
206 Созаемщик-Рабочий

тип телефона''', 'magenta'), colored(u'''
1   Не звонили ни разу
2   Результата не было
3   Неверный номер
4   Результат
5   Последний результат
6   Автоинформатор

статус телефона''', 'magenta'))
            ]

            ,'perspect': [perspect,
                           colored(u'даты и количество '
                                   u'перспективных контактов по долгу', 'green'),
                           (colored(u'даты', 'magenta'), colored(u'количество', 'magenta'))
            ]

        }

        self.concate = u'''
SELECT top 10
    count(d.id)
FROM
    i_collect.dbo.bank as b
    inner join i_collect.dbo.portfolio as p on b.id = p.parent_id
    inner join i_collect.dbo.debt as d on p.id = d.r_portfolio_id
    inner join i_collect.dbo.person as per on d.parent_id = per.id
'''

    def concatenator(self):

        """ concatenate SQL parts """

        print colored(u'\nТеперь выбираем модули\nПросто напиши '
                      u'через запятую модули, которые будешь использовать\n\n\n', 'green')
        for k, v in sorted(self.try_dict.items()):
            print '\n', k, colored('-', 'magenta'), v[1]

        r = raw_input(colored(u'\n\n\n\nimport: ', 'magenta'))
        print u'\n'
        r = r.replace(' ', '').split(',')

        result_query = self.concate
        for module in r:
            if module in self.try_dict:
                query, description, fields = self.try_dict[module]
                params = []
                print description
                for field in fields:
                    value = raw_input('%s : ' % field)
                    params.append(value)
                query = query % tuple(params)
                result_query = u'\n'.join([result_query, query])
        self.first_query = result_query
        return result_query
