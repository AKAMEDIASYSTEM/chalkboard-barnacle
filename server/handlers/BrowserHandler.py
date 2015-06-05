#!/usr/bin/env python
# tuned-resonator cafe-barnacle

import logging
import tornado
from handlers.BaseHandler import BaseHandler


class BrowserHandler(BaseHandler):
    '''HTML display of the chalkboard'''

    def get(self):
        MAX_MSGS = 10
        loader = tornado.template.Loader('server/templates')
        # n = self.get_argument('n', 3)
        db = self.settings['db']
        logging.debug('hit the BrowserHandler endpoint')
        k = db.lrange('msgs', 0, MAX_MSGS)
        if k is None:
            k = ['no messages right now']
        self.write(loader.load("main.html").generate(keywords=k))
        self.finish()

    def post(self):
        db = self.settings['db']
        utterance = self.get_argument('utterance', None)
        print 'inside chalkboard-barnacle SubmitHandler', utterance
        if utterance is not None:
            try:
                db.lpush(str(utterance))
            except:
                print 'there was a big problem with ', utterance
        self.response = ResponseObject('200', 'Success')
        self.write_response()
        self.finish()