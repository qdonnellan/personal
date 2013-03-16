import webapp2
from handlers import MainHandler

class MainPage(MainHandler):
  def get(self):
    self.render('home.html', home_active ="active")

app = webapp2.WSGIApplication([
  ('.*', MainPage)
  ],debug=True)
     