# Copyright (C) 2013 Quentin Donnellan
# License: MIT (http://opensource.org/licenses/MIT)
# www.qdonnellan.com

import unittest
from blog import api

class blogAPItest(unittest.TestCase):
  known_blog_posts = [
    ['2013', '07', '21'],
  ]
  def test_fetch_blog_post(self):
    for blog_post in self.known_blog_posts:
      year, month, day = blog_post
      self.assertIsNotNone(api().fetch_blog_post(year, month, day), 'fetching of blog post %s failed' % blog_post)