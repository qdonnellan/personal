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

from google.appengine.ext import ndb

class blogContent(ndb.Model):
  title = ndb.StringProperty(required = True)
  body = ndb.TextProperty(required = False)
  last_modified = ndb.DateTimeProperty(auto_now = True)
  created = ndb.DateTimeProperty(auto_now_add = True)

def editBlogContent(title, body, contentID=None):
  if contentID is None:
    content = blogContent(title = title, body = body)
    content.put()
  else:
    key = ndb.Key(blogContent, int(contentID))
    content = key.get()
    content.populate(title = title, body = body)
    content.put()

def getBlog(contentID = None, get_all=False):
  if get_all:
    return blogContent.query().order(-blogContent.created)
  elif contentID is not None:
    key = ndb.Key(blogContent, int(contentID))
    return key.get()
  else:
    return None


