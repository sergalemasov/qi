# -*- coding: utf-8 -*-
import os
from cmd_wrapper import CmdWrapper


class FirstStepAfterAnimation(object):
    """Ask a manager about start of Q-Interpreter"""

    @staticmethod
    def start_or_not():

        ask_continue = raw_input(u'\n\n\nПродолжаем? y \ n:   ')
        if ask_continue in u'Nn':
            print u'До новых встреч!'
            exit()
        else:
            CmdWrapper.cls()

