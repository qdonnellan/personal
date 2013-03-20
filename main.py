import webapp2
from handlers import MainHandler
from google.appengine.api import users
import database
from format import formatContent

class MainPage(MainHandler):
  def get(self):
    self.render('home.html', home_active ="active")

class BlogPage(MainHandler):
  def get(self):
    self.render('blog.html', 
      blog_active = "active", 
      admin = users.is_current_user_admin(),
      blog_content = formatContent(database.getBlog(get_all = True)))

class AuthPage(MainHandler):
  def get(self):
    self.render('auth.html',
      logoffURL = users.create_logout_url('/'),
      loginURL = users.create_login_url('/'))

class EditBlog(MainHandler):
  def get(self, contentID=None):
    if users.is_current_user_admin():
      existingContent = database.getBlog(contentID = contentID)
      self.render('edit_blog.html', content = existingContent)

  def post(self, contentID=None):
    if users.is_current_user_admin():
      title = self.request.get('title')
      body = self.request.get('body')
      database.editBlogContent(title, body, contentID)
      self.redirect('/blog')

app = webapp2.WSGIApplication([
  ('/blog', BlogPage),
  ('/auth', AuthPage),
  ('/edit_blog', EditBlog),
  ('/edit_blog/(\w+)', EditBlog),
  ('.*', MainPage)
  ],debug=True)
     