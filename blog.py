# Copyright (C) 2013 Quentin Donnellan
# License: MIT (http://opensource.org/licenses/MIT)
# www.qdonnellan.com

from handlers import MainHandler
import os
import json
import re
import markdown2

class blogAPI(MainHandler):
  def get(self, year=None, month=None, day=None):
    if year == 'latest':
      data = self.get_latest()
    elif year == 'map':
      data = self.get_map()
    else:
      data = self.fetch_blog_post(year, month, day)
    self.response.headers['Content-Type'] = 'application/json' 
    self.response.out.write(data)

  def get_latest(self):
    return self.fetch_blog_post('2014', '01', '04')

  def get_map(self):
    blog_dir = os.path.join(os.path.dirname(__file__),"blog_files")
    path = blog_dir + "/blogmap.json"
    with open(path, 'r') as f:
      blog_map = f.read()
    f.closed
    return blog_map

  def fetch_blog_post(self, year, month, day):
    # returns dictionary object of blog post
    # blog posts are stored in ../blog_files/YEAR/MONTH/DAY.md
    # blog posts should be writtne in the form of:
    #--:
    #--: # Titile
    #--: author: Someone's Name
    #--:
    #--: Post content starts here
    #--:

    blog_dir = os.path.join(os.path.dirname(__file__),"blog_files")
    blog_path = blog_dir + "/{y}/{m}_{d}.md".format(y = year, m = month, d = day)
    with open(blog_path, 'r') as f:
      blog_data = f.read()
    f.closed
    title = re.search('[#].*\n', blog_data).group()
    author = re.search('author:.*\n', blog_data)
    if author:
      author = author.group()
      blog_data = re.sub(author, '', blog_data)
      author = re.sub('author:', '', author).strip('\n')
    else:
      author = 'Quentin Donnellan'

    blog_data = re.sub(title, '', blog_data).strip('\n')
    
    title = re.sub('[#]', '', title).strip('\n')
    data = {
      'year' : year,
      'day' : day, 
      'month' : month,
      'author' : author.strip(' '),
      'markdown' : blog_data,
      'html' : markdown2.markdown(blog_data),
      'title' : title.strip(' ')
      }
    return json.dumps(data)
