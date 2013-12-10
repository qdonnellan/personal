from handlers import MainHandler
import os
import json
import re

class blogAPI(MainHandler):
  def get(self, year=None, month=None, day=None):
    if year == 'latest':
      year, month, day = '2013', '07', '21'
    data = self.fetch_blog_post(year, month, day)
    self.response.headers['Content-Type'] = 'application/json' 
    self.response.out.write(json.dumps(data))

  def active_blogs(self):
    active_list = [
      ('2013', '07', '21'),
      ('2013', '07', '19'),
      ('2013', '03', '27'),
    ]
    active_list = [self.fetch_blog_post(year, month, day) for year, month, day in active_list]
    return active_list

  def fetch_blog_post(self, year, month, day):
    # returns JSON object of blog post
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
      'content' : blog_data,
      'title' : title.strip(' ')
      }

    return data
