#!/usr/bin/env python

# AKA tuned-resonator cafe server (scratch)
import tornado.ioloop
import tornado.web
from handlers.BrowserHandler import BrowserHandler
# from handlers.SubmitHandler import SubmitHandler
import redis

settings = {'debug': True}
db = redis.StrictRedis(host='localhost', port=6379, db=0)

application = tornado.web.Application([
    # (r"/api", ApiHandler),
    (r"/", BrowserHandler),
    # (r"/submit", SubmitHandler),
], db=db, **settings)

if __name__ == "__main__":
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()


'''
simple, simple single page message board
only the last 60 minutes' messages are shown
OR
only the last 5 messages are shown

no logins, _maybe_ an optional field for a name

no photos, but make it so photos-of-space
can be added later with a webcam or something


hammeraspce -> utility? strict utility?

speedtest - useful, immediate-environment thing
temperature - not much you can do about knowing the temp in the Here and Now

curriculum - "sense" social/semantic aspect of the environment in the Here and Now

cafe - "communicate"

pseudocode:
on GET:
    search for X latest strings in redis "msgs" store
    shove these into a simple template file
    template file allows anyone to submit text as well
    that submittion POSTS to /submit




'''
