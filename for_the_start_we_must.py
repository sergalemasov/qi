# -*- coding: utf-8 -*-
from termcolor import colored


class ForTheStartWeMust(object):
    """Print what we gonna do"""

    @staticmethod   
    def start_func():
        start = u'\n\nДля начала мы выберем Банк(-и) и Портфель(-и)\n'
        print colored(start, 'green')