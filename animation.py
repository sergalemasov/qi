# -*- coding: utf-8 -*-
import os
from termcolor import colored
from cmd_wrapper import CmdWrapper

ROWS = [
    colored(x, y) for (x, y) in [
        (u'███████ ─── ██████████████████████████████████████████████████', 'white'),
        (u'█────██ ─── █───█─██─█───█───█────█────█────█───█───█───█────█', 'white'),
        (u'█─██─██ ─── ██─██──█─██─██─███─██─█─██─█─██─█─████─██─███─██─█', 'blue'),
        (u'█─█──██ ─── ██─██─█──██─██───█────█────█────█───██─██───█────█', 'blue'),
        (u'█─██─██ ─── ██─██─██─██─██─███─█─██─████─█─██─████─██─███─█─██', 'blue'),
        (u'█─██─██ ─── ██─██─██─██─██─███─█─██─████─█─██─████─██─███─█─██', 'blue'),
        (u'█─────█ ─── █───█─██─██─██───█─█─██─████─█─██───██─██───█─█─██', 'red'),
        (u'█████─█ ─── ██████████████████████████████████████████████████', 'red')
    ]
]


class QiHi(object):
    """Logo Animation"""

    @staticmethod
    def qi_rus():
        j = ''
        # big animations minimized to loops:
        for i in (range(7) + range(5, 0, -1)):
            print u'\n' * (i + 2), ROWS[i]
            CmdWrapper.cls()

        for i in range(1, 8):
            j = u'\n\n' + u'\n'.join(ROWS[0:i])
            print u'\n\n' + u'\n'.join(ROWS[0:i])
            CmdWrapper.cls()

        print j