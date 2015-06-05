#!/usr/bin/env python
# tuned-resonator
# experiments with google physical-web mdns broadcast

from handlers.BaseHandler import BaseHandler
from ResponseObject import ResponseObject


class SubmitHandler(BaseHandler):
    """form submission to chalkboard redis"""

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
