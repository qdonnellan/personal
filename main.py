# Copyright (C) 2013 Quentin Donnellan
# License: MIT (http://opensource.org/licenses/MIT)
# www.qdonnellan.com

import webapp2
from handlers import MainHandler
import logging
import markdown2
from blog import blogAPI

class MainPage(MainHandler):
  def get(self):
    self.render('home.html', home_active ="active")

app = webapp2.WSGIApplication([
  ('/api/blog/(\w+)/(\w+)/(\w+)', blogAPI),
  ('/api/blog/(\w+)', blogAPI),
  ('.*', MainPage)
  ],debug=True)
