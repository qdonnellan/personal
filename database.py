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


