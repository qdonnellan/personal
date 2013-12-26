# Copyright (C) 2013 Quentin Donnellan
# License: MIT (http://opensource.org/licenses/MIT)
# www.qdonnellan.com

import webapp2
from handlers import MainHandler
from blog import blogAPI

class MainPage(MainHandler):
  def get(self):
    self.render('home.html', home_active ="active")

class BlogPage(MainHandler):
  def get(self):
    self.render('blog.html', home_active ="active", page_name = "blog")

app = webapp2.WSGIApplication([
  ('/api/blog/(\w+)/(\w+)/(\w+)', blogAPI),
  ('/api/blog/(\w+)', blogAPI),
  ('/blog', BlogPage),
  ('.*', MainPage)
  ],debug=True)
