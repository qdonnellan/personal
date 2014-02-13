import json

from main_view_handler import ViewHandler
from controllers.jsonify_blog_post import jsonify_blog_post

class BlogPage(ViewHandler):
    '''
    handler for the blog page view
    '''
    def get(self, year=None, month=None, day=None):
        '''
        handle the get request
        '''
        blog_json = jsonify_blog_post(year, month, day)

        self.render('blog.html', 
            home_active ="active", 
            page_name = "blog",
            blogJSON = blog_json,
            blogMAP = [])