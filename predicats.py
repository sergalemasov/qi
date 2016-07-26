# -*- coding: utf-8 -*-
from termcolor import colored



class Predicats(object):
    """Show simple predicats"""
    @staticmethod
    def show_predicats(user):
        # False means, that chunk will be colored by default cli color.
        text_chunks = [
            (u'\n\nПриветствую тебя', 'yellow'),
            (user, False),
            (u'\nДобро пожаловать в систему Q-Interpreter 0.1\n', 'yellow'),
            (u'\n\n\n\n\n\nИспользуй стандартные '
             u'SQL предикаты для параметризации, такие как:\n\n', 'green'),
            (u'in', 'magenta'),
            (u'список, например', False),
            (u'in (49, 14)\n', 'magenta'),
            (u'not in', 'magenta'),
            (u'список исключений, например', False),
            (u'not in (6,7,8,10)\n', 'magenta'),
            (u'=', 'magenta'), 
            (u'равно\n', False),
            (u'!=', 'magenta'), 
            (u'не равно\n', False),
            (u'>', 'magenta'), 
            (u'больше\n', False),
            (u'<', 'magenta'), 
            (u'меньше\n', False),
            (u'>=', 'magenta'), 
            (u'больше или равно\n', False),
            (u'<=', 'magenta'), 
            (u'меньше или равно\n', False),
            (u'!<', 'magenta'), 
            (u'не меньше\n', False),
            (u'!>', 'magenta'), 
            (u'не больше\n', False),
            (u'between', 'magenta'), 
            (u"между, например", False), 
            (u"between '01-01-2015' and 07-07-2016\n", 'magenta')
        ]

        text = ""
        for chunk in text_chunks:
            if not chunk[1]:
                text += chunk[0]
            else:
                text += colored(*chunk)
            # add space if chunk not followed by line feed
            if not chunk[0].endswith('\n'):
                text += " "
        print text