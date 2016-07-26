# -*- coding: utf-8 -*-
import os

from cmd_wrapper import CmdWrapper
from query_i_collect import QueryICollect, bank, portfolio
from termcolor import colored


bpl = ''  # используется для конкатенации (тут банк и портфель)


class BankAndPortfParam(object):
    """Param bank and portfolio string for concatenate"""

    bank_list = u'\nWHERE\n     b.id {}\n'  # первое условие со списком банков
    portfolio_list = u'     and p.id {0}\n'  # условие
    bank_inp = None
    port_inp = None

    def bank(self):
        global bpl
        queryObj = QueryICollect()
        # open DB connection
        queryObj.connect()

        print queryObj.two(bank)  # показываем список открытых банков
        bank_input = raw_input(colored(u'\nБанк(-и):   ', 'magenta'))  # выбираем список банков
        bpl += self.bank_list.format(bank_input)
        CmdWrapper.cls()

        print queryObj.two(portfolio.format(bank_input))  # показываем список портфелей выбранных банков
        self.port_inp = raw_input(colored(u'\nПортфель(-и):  ', 'magenta'))  # выбираем список портфелей
        bpl += self.portfolio_list.format(self.port_inp)
        CmdWrapper.cls()
        
        # close DB connection
        queryObj.close()
        return bpl

    def ret(self):
        return bpl


# if __name__ == '__main__':
#     BankAndPortfParam()
