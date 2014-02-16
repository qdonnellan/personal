import json

from main_view_handler import ViewHandler
from controllers.jsonify_blog_post import jsonify_blog_post

class SingleBlogPage(ViewHandler):
    '''
    handler for the blog page view
    '''
    def get(self, year=None, month=None, day=None):
        '''
        handle the get request
        '''
        blog = jsonify_blog_post(year, month, day)
        self.render('single_blog_page.html', blog = json.loads(blog))