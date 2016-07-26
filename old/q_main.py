# -*- coding: utf-8 -*-
import codecs
import sys

from termcolor import colored
from first_concatenator import FirstModuleList
from second_concatenator import SecondModuleList
from colorama import init
from animation import QiHi
from predicats import Predicats
from bank_and_portf import BankAndPortfParam
from first_step_after_animation import FirstStepAfterAnimation
from for_the_start_we_must import ForTheStartWeMust
from simple_query import simple_query
from cmd_wrapper import CmdWrapper
from query_wh_data import QueryWhData
from query_i_collect import QueryICollect, bank, portfolio, phone_typ
from exec_query import ExecQueryICollect, ExecQueryWhData

# подключаем русский язык
sys.stdout = codecs.getwriter('cp866')(sys.stdout, 'replace')


def main():
    """Start Main() of Q-Interpreter"""
    init()
    CmdWrapper.cmd_size()
    CmdWrapper.yellow()
    QiHi().qi_rus()  # Animations
    Predicats().show_predicats()  # показываем SQL предикаты
    FirstStepAfterAnimation().start_or_not()  # продолжаем работать с программой
    ForTheStartWeMust().start_func()  # показываем для начала выбрать банк и портфель
    BankAndPortfParam().bank()  # выбираем банки и портфели

    x = FirstModuleList().concatenator() + BankAndPortfParam().ret() + SecondModuleList().concatenator_2()
    print x
    print colored(simple_query(x), 'magenta')


if __name__ == '__main__':
    while True:
        main()
        a = raw_input(colored(u'Еще разок? y \ n :  ', 'green'))
        if a in u'Nn':
            exit()
        else:
            continue
