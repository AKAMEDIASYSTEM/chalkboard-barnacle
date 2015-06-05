#!/usr/bin/env python
# tuned-resonator cafe-barnacle

import logging
import tornado
from handlers.BaseHandler import BaseHandler


class BrowserHandler(BaseHandler):
    '''HTML display of Keywords browsed in the last day'''

    MAX_MSGS = 10

    def get(self):
        loader = tornado.template.Loader('../server/templates')
        # n = self.get_argument('n', 3)
        db = self.settings['db']
        logging.debug('hit the BrowserHandler endpoint')
        keywords = []
        found = 0
        k = db.lrange('msgs',0,MAX_MSGS)
        if k is None:
            k = ['no messages right now']
        self.write(loader.load("main.html").generate(keywords=k))
        self.finish()
