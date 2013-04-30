# Copyright (C) 2013 Quentin Donnellan
# http://qdonnellan.appspot.com
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import webapp2
from handlers import MainHandler
from google.appengine.api import users
import database
from format_lite import formatContent
from google.appengine.api import mail
import logging
import json

class MainPage(MainHandler):
  def get(self):
    self.render('home.html', home_active ="active")

class StaticPage(MainHandler):
  def get(self,page_name):
    if page_name in ['work', 'about', 'contact']:
      self.render('%s.html' % page_name)
    else:
      self.redirect('/')

  def post(self,page_name):
      try:
        message = mail.EmailMessage(
          sender="qdonnellan Support <qdonnellan@gmail.com>",
          subject='EMAIL FROM APPSPOT WEBSITE:' + self.request.get('email_subject'),
          to = 'qdonnellan@gmail.com',
          reply_to = self.request.get('email_addy'),
          body = self.request.get('email_message'))
        message.send()
      except Exception as e:
        self.redirect('/contact?error=There was a problem sending your email: %s' % e)
      else:
        self.redirect('/contact?success=Your email has been sent!')

class BlogPage(MainHandler):
  def get(self):
    self.render('blog.html', 
      blog_active = "active", 
      admin = users.is_current_user_admin(),
      blog_content = formatContent(database.getBlog(get_all = True)))

class BlogPermalink(MainHandler):
  def get(self, postID):
    self.render('blog.html', 
      single_post = True, 
      admin = users.is_current_user_admin(),
      blog_content = formatContent([database.getBlog(contentID = postID)]))

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

class practice(MainHandler):
  def get(self):
    with open('ccss.json', 'rb') as f:
      ccss = json.load(f)
    f.closed
    current_standards = self.request.get('standards')
    current_standards = current_standards.split('|')
    namemap = {
      '1' : 'Grade 1',
      '2' : 'Grade 2', 
      '3' : 'Grade 3', 
      '4' : 'Grade 4',
      '5' : 'Grade 5', 
      '6' : 'Grade 6', 
      '7' : 'Grade 7',
      '8' : 'Grade 8', 
      '6-8' : 'Grades 6-8', 
      '9-10' : 'Grades 9-10',
      '11-12' : 'Grades 11-12', 
      'K' : 'Kindergarten', 
      'RH' : 'History/Social Studies',
      'RST' : 'Science & Technical Subjects',
      'Practice' : 'Mathematical Practice',
      'HSN' : 'High School: Number and Quantity',
      'HSA' : 'High School: Algebra',
      'HSF' : 'High School: Functions',
      'HSG' : 'High School: Geometry',
      'HSS' : 'High School: Statistics & Probability',
      'CCRA' : 'College and Career Readiness Anchor Standards (CCRAS)',
      'RL' : 'Reading: Literature',
      'RI' : 'Reading: Informational Text',
      'RF' : 'Reading: Foundational Skills', 
      'W' : 'Writing',
      'SL' : 'Speaking & Listening',
      'L' : 'Language',
      'R' : 'Reading',
      'WHST' : 'Writing for History/Social Studies, Science, & Technical Subjects',
      'CCRA-R' : 'Anchor Standards for Reading',
      'CCRA-W' : 'Anchor Standards for Writing',
      'CCRA-SL' : 'Anchor Standards for Speaking & Listening',
      'CCRA-L' : 'Anchor Standards for Language',
      

    }
    with open('teks.json', 'rb') as f:
      teks = json.load(f)
    f.closed
    self.render('practice.html', ccss=ccss, namemap = namemap, current_standards = current_standards, teks=teks)
  def post(self):
    standards = self.request.get_all('standards-checked')
    q = 'standards='
    for standard in standards:
      q+= standard+'|'
    self.redirect('/practice?%s' % q)

class practiceteks(MainHandler):
  def get(self):
    with open('teks.json', 'rb') as f:
      teks = json.load(f)
    f.closed
    self.render('practiceteks.html', teks=teks)
    

app = webapp2.WSGIApplication([
  ('/blog', BlogPage),
  ('/blog/(\w+)', BlogPermalink),
  ('/auth', AuthPage),
  ('/edit_blog', EditBlog),
  ('/edit_blog/(\w+)', EditBlog),
  ('/practice/ccss', practice),
  ('/practice/teks', practiceteks),
  ('/(\w+)', StaticPage),
  ('.*', MainPage)
  ],debug=True)
