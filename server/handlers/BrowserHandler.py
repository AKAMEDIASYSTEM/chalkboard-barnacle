#!/usr/bin/env python
# tuned-resonator cafe-barnacle

import logging
import tornado
from handlers.BaseHandler import BaseHandler


class BrowserHandler(BaseHandler):
    '''HTML display of the chalkboard'''

# define a timeout object here

    def get(self):
        # here you should cancel any pending timeout
        MAX_MSGS = 10
        loader = tornado.template.Loader('server/templates')
        # n = self.get_argument('n', 3)
        db = self.settings['db']
        logging.debug('hit the BrowserHandler endpoint')
        k = db.lrange('msgs', 0, MAX_MSGS)
        if k is None:
            k = ['no messages right now|192.168.1.1']
        # thinking about using color-of-text-background to
        # associate utterances with subnet addresses?
        # address is available at self.request.remote_ip
        # k.append(self.request.remote_ip)

        self.write(loader.load("main.html").generate(keywords=k))
        # here you should activate any pending timeout
        # (when timeout occurs, we write the time in a nicely-formatted string to the redis store)
        # this means utterances expire once 10 timeouts have occurred
        # which means nobody has been active for 10*timeout minutes
        self.finish()

    def post(self):
        MAX_MSGS = 10
        db = self.settings['db']
        loader = tornado.template.Loader('server/templates')
        # entangle IP address w utterance
        utterance = '|'.join([self.get_argument('utterance', None), self.request.remote_ip])
        print 'inside chalkboard-barnacle SubmitHandler', utterance
        if utterance is not None:
            try:
                db.lpush('msgs', str(utterance))
            except:
                print 'there was a big problem with ', utterance
            db.ltrim('msgs', 0, MAX_MSGS)  # trim with every submission, FIFO not expiring for now
        k = db.lrange('msgs', 0, MAX_MSGS)
        if k is None:
            k = ['no messages right now']
        self.write(loader.load("main.html").generate(keywords=k))
        self.finish()
