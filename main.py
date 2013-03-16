import webapp2
from handlers import MainHandler

class MainPage(MainHandler):
  def get(self):
    self.render('home.html')

app = webapp2.WSGIApplication([
  ('.*', MainPage)
  ],debug=True)
     