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
        self.render('blog.html')