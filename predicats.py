# -*- coding: utf-8 -*-
from colorama import init
from termcolor import colored
import getpass

init()

user = getpass.getuser()


class Predicats(object):
    """Show simple predicats"""

    def show_predicats(self):
        print colored(u'\n\nПриветствую тебя', 'yellow') \
            , user, colored(u'\nДобро пожаловать в '
                            u'систему Q-Interpreter 0.1\n', 'yellow')
        print colored(u'\n\n\n\n\nИспользуй стандартные '
                      u'SQL предикаты для параметризации, такие как:\n', 'green')
        print colored(u'in', 'magenta') \
            , u'список, например', \
            colored('in (49, 14)', 'magenta')
        print colored(u'not in', 'magenta'), u'список исключений, например', \
            colored(u'not in (6,7,8,10)', 'magenta')
        print colored(u'=', 'magenta'), u'равно'
        print colored(u'!=', 'magenta'), u'не равно'
        print colored(u'>', 'magenta'), u'больше'
        print colored(u'<', 'magenta'), u'меньше'
        print colored(u'>=', 'magenta'), u'больше или равно'
        print colored(u'<=', 'magenta'), u'меньше или равно'
        print colored(u'!<', 'magenta'), u'не меньше'
        print colored(u'!>', 'magenta'), u'не больше'
        print colored(u'between', 'magenta') \
            , u"между, например", colored(u"between '01-01-2015' "
                                          u"and 07-07-2016", 'magenta')
