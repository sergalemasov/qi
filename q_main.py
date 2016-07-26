# -*- coding: utf-8 -*-
import codecs
import colorama
import getpass
import sys

from animation import QiHi
from bank_and_portf import BankAndPortfParam
from cmd_wrapper import CmdWrapper
from first_step_after_animation import FirstStepAfterAnimation
from for_the_start_we_must import ForTheStartWeMust
from predicats import Predicats
from termcolor import colored


COLORAMA_INITIALIZED = False

def main():
    # local_vars    
    cmd_color = "yellow"
    cmd_lines = 49
    # catching current user
    user = getpass.getuser()

    global COLORAMA_INITIALIZED
    # initializing colorama
    if COLORAMA_INITIALIZED:
        colorama.reinit()
    else:
        COLORAMA_INITIALIZED = True
        colorama.init()
    # defining cmd window space
    CmdWrapper.cmd_size(cmd_lines)
    # defining cmd color
    CmdWrapper.cmd_color(cmd_color) 
    # starting animation Q INTERPRETER
    QiHi.qi_rus()
    # showing SQL predicates
    Predicats.show_predicats(user)

    FirstStepAfterAnimation.start_or_not()
    ForTheStartWeMust.start_func()

    bankObj = BankAndPortfParam()
    bankObj.bank()  # выбираем банки и портфели
    # далее вместо BankAndPortfParam() просто делаешь bankObj.метод 
    # (bankObj.ret())

    # clearing vars
    user = None


def main_loop():
    main()
    while True:
        a = raw_input(colored(u'Еще разок? y/n : ', 'green'))
        while a not in u'yYnN':
            a = raw_input(colored(u'Y or N?! : ', 'green'))
        if a in u'Nn':
            colorama.deinit()
            sys.exit(0)
        else:
            main()


if __name__ == '__main__':
    main_loop()    