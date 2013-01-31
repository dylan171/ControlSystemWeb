# coding=UTF-8
'''
Initialize Web Site
'''

from twisted.web.server import Site
from twisted.web.resource import Resource

webroot = Resource()
log.msg('website.py: Root Resource: %(r)s', r=webroot, logLevel=_TRACE)

website = Site(webroot)
log.msg('website.py: Root Resource: %(r)s', r=webroot, logLevel=_TRACE)

webport = 8080
reactor.listenTCP(webport, website)
log.msg('website.py: Website listening on port: %(p)s', p=str(webport), logLevel=_DEBUG)