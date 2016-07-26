# -*- coding: utf-8 -*-
import os


class CmdWrapper(object):
    """cmd options"""

    @staticmethod
    def magenta():
        os.system('color d')

    @staticmethod
    def white():
        os.system('color f')

    @staticmethod
    def yellow():
        os.system('color e')

    @staticmethod
    def white():
        os.system('color f')

    @staticmethod
    def cls():
        os.system('cls')

    @staticmethod
    def cmd_size():
        os.system('mode con lines=49')


