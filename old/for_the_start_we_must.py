# -*- coding: utf-8 -*-
from colorama import init
from termcolor import colored
init()


class ForTheStartWeMust(object):
    """Print what we gonna do"""

    start = u'\n\nДля начала мы выберем Банк(-и) и Портфель(-и)\n'

    def start_func(self):
        print colored(self.start, 'green')