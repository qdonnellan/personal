from main_view_handler import ViewHandler
from controllers.jsonify_blog_post import jsonify_blog_post
from controllers.fetch_blog_map import fetch_blog_map

class BlogAPI(ViewHandler):
    '''
    the class for request to the blog api, always returns json objects
    '''
    def get(self, year=None, month=None, day=None):
        '''
        the get request
        '''
        if year == 'latest':
            data = jsonify_blog_post('2014', '01', '10')
        elif year == 'map':
            data = fetch_blog_map()
        else:
            data = jsonify_blog_post(year, month, day)

        self.response.headers['Content-Type'] = 'application/json' 
        self.response.out.write(data)



