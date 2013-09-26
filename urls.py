# -*- coding: utf-8 -*-
'''
Created on Sept 26, 2013

@author: Rafael Nunes
'''


import webapp2

from core.page_handlers import *

routes = [('/', IndexPage),]

app = webapp2.WSGIApplication(routes, debug=True)
