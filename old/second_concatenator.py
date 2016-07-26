# -*- coding: utf-8 -*-
from colorama import init
from termcolor import colored
from cmd_wrapper import CmdWrapper

init()


class SecondModuleList(object):
    """concatenate behavior part of SQL queries"""

    first_query = None

    def __init__(self):
        self.try_dict = {

            'product': [
                u'     and d.typ %s\n'
                ,colored(u'Тип продукта \n\n1: авто\n2:Ипотека\nРитейл', 'green')
                ,(colored(u'тип', 'magenta'),)
            ]

            ,'bdpd': [

                u'     and datediff(day, d.start_date, p.sign_date) %s \n'
                ,colored(u'Банковская просрочка', 'green')
                ,(colored(u'Просрочка', 'magenta'),)
            ]

            , 'fdpd': [

                u'     and datediff(day,d.start_date,getdate()-1) %s \n'
                ,colored(u'Фактическая просрочка', 'green')
                ,(colored(u'Просрочка', 'magenta'),)
            ]

            , 'percent_rate': [

                u'     and (d.interest_rate %s )\n'
                ,colored(u'Процентная ставка', 'green')
                ,(colored(u'Ставка', 'magenta'),)
            ]

            , 'dstat': [

                u'     and d.status %s\n'
                , colored(u'Статус долга ', 'green')
                , (colored(u'статус', 'magenta'),)
            ]

            , 'dsum': [

                u'     and d.debt_sum %s\n'
                , colored(u'Остаток долга ', 'green')
                , (colored(u'Остаток', 'magenta'),)
            ]

            , 'psign': [

                u'     and p.sign_date %s\n'
                , colored(u'Вход портфеля ', 'green')
                , (colored(u'Дата(-ы)', 'magenta'),)
            ]

            , 'days_out': [

                u'     and datediff(day, getdate(), end_date) %s\n'
                , colored(u'Дней до выхода портфеля ', 'green')
                , (colored(u'Дней', 'magenta'),)
            ]
        }

        self.concate = u'     and 1=1\n'

    def concatenator_2(self):
        """ concatenate SQL parts """

        CmdWrapper.cls()
        print colored(u'\nОсталось выбрать еще несколько модулей\nПросто напиши '
                      u'через запятую, модули, которые будешь использовать\n\n\n', 'green')
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

