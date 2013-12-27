# Copyright (C) 2013 Quentin Donnellan
# License: MIT (http://opensource.org/licenses/MIT)
# www.qdonnellan.com

import webapp2
from handlers import MainHandler
from blog import blogAPI
import json
import logging

class MainPage(MainHandler):
  def get(self):
    self.render('home.html', home_active ="active")

class BlogPage(MainHandler):
  def get(self, year=None, month=None, day=None):
    blog = blogAPI()
    if not any([year, month, day]):
      blogJSON = blog.get_latest()
    else:
      blogJSON = blog.fetch_blog_post(year, month, day)
    self.render('blog.html', 
      home_active ="active", 
      page_name = "blog",
      blogJSON = json.loads(blogJSON),
      blogMAP = json.loads(blog.get_map()))

app = webapp2.WSGIApplication([
  ('/api/blog/(\w+)/(\w+)/(\w+)', blogAPI),
  ('/api/blog/(\w+)', blogAPI),
  ('/blog/(\w+)/(\w+)/(\w+)', BlogPage),
  ('/blog', BlogPage),
  ('.*', MainPage)
  ],debug=False)
