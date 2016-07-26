# -*- coding: utf-8 -*-
import os

from query_i_collect import QueryICollect, bank, portfolio
from colorama import init
from termcolor import colored


init()

bpl = ''  # используется для конкатенации (тут банк и портфель)


class BankAndPortfParam(object):
    """Param bank and portfolio string for concatenate"""

    bank_list = u'\nWHERE\n     b.id {}\n'  # первое условие со списком банков
    portfolio_list = u'     and p.id {0}\n'  # условие
    bank_inp = None
    port_inp = None

    @staticmethod
    def _clear():
        os.system('cls')

    def bank(self):
        global bpl
        print QueryICollect(bank).two  # показываем список открытых банков
        bank_input = raw_input(colored(u'\nБанк(-и):   ', 'magenta'))  # выбираем список банков
        bpl += self.bank_list.format(bank_input)
        self._clear()

        print QueryICollect(portfolio.format(bank_input)).two  # показываем список портфелей выбранных банков
        self.port_inp = raw_input(colored(u'\nПортфель(-и):  ', 'magenta'))  # выбираем список портфелей
        bpl += self.portfolio_list.format(self.port_inp)
        self._clear()
        return bpl

    def ret(self):
        return bpl


# if __name__ == '__main__':
#     BankAndPortfParam()
