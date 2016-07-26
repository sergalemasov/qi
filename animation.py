# -*- coding: utf-8 -*-
import os
from termcolor import colored

# a lot of colored() minimized to list generator
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
    def _yellow_cmd_color():
        os.system('color e')

    @staticmethod
    def _clear_screen():
        os.system('cls')

    def qi_rus(self):
        j = ''
        # making yellow cli color
        self._yellow_cmd_color()

        # big animations minimized to loops:
        for i in (range(7) + range(5, 0, -1)):
            print u'\n' * (i + 2), ROWS[i]
            self._clear_screen()

        for i in range(1, 8):
            j = u'\n\n' + u'\n'.join(ROWS[0:i])
            print u'\n\n' + u'\n'.join(ROWS[0:i])
            self._clear_screen()

        print j

# FIXME if this program is Main()
# if __name__ == '__main__':
#     init()
#     QiHi().qi_rus()
