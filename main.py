import webapp2

from views.front_page import FrontPage
from views.blog_page import BlogPage
from views.blog_api import BlogAPI

app = webapp2.WSGIApplication([
    ('/api/blog/(\w+)/(\w+)/(\w+)', BlogAPI),
    ('/api/blog/(\w+)', BlogAPI),
    ('/blog/(\w+)/(\w+)/(\w+)', BlogPage),
    ('/blog', BlogPage),
    ('.*', FrontPage)
    ],debug=False)
