from controllers.fetch_blog_map import fetch_blog_map
from base_test_handler import TestHandler

import json

class FetchBlogMapTest(TestHandler):
    '''
    test the the controller for fetching the blog map json object
    '''

    def test_fetch_blog_map_json_object(self):
        '''
        fetching the blog map should return something that is not none!
        '''
        json_blog_map = fetch_blog_map()
        self.assertIsNotNone(json_blog_map)

        data = json.loads(json_blog_map)
        self.assertEqual(len(data), 11)

        