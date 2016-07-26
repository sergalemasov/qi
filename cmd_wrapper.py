# -*- coding: utf-8 -*-
import os

class CmdWrapper(object):
    """cmd options"""

    @staticmethod
    def cmd_color(color):
        color_dct = {
            "yellow": "e",
            "white": "f",
            "magenta": "d"
        }
        # raises assertion error if color is incorrect
        assert color in color_dct.keys()
        os.system('color %s' % color_dct[color])

    @staticmethod
    def cls():
        os.system('cls')

    @staticmethod
    def cmd_size(cmd_lines):
        os.system('mode con lines=%d' % cmd_lines)
