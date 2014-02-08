import json

from main_view_handler import ViewHandler
from blog_json import get_latest, fetch_blog_post

class BlogPage(ViewHandler):
    '''
    handler for the blog page view
    '''
      def get(self, year=None, month=None, day=None):
        '''
        handle the get request
        '''
        blog = blogAPI()
        if not any([year, month, day]):
            blogJSON = get_latest()
        else:
            blogJSON = fetch_blog_post(year, month, day)

        self.render('blog.html', 
            home_active ="active", 
            page_name = "blog",
            blogJSON = json.loads(blogJSON),
            blogMAP = json.loads(blog.get_map()))