from controllers.jsonify_blog_post import jsonify_blog_post
from controllers.fetch_blog_post import fetch_blog_post
from base_test_handler import TestHandler

import json

class JsonifyBlogPostTest(TestHandler):
    '''
    test the the controller for turning blog posts into a json object
    '''

    def test_jsonify_blog_post_for_known_blog_file(self):
        '''
        test a call to jsonify a known blog posts returns the expected json object
        '''
        json_blog_object = jsonify_blog_post('2014','01','03')
        self.assertIsNotNone(jsonify_blog_post)

        blog_data = json.loads(json_blog_object)
        self.assertEqual("10 Posts in 10 Days", blog_data['title'])
        self.assertEqual('2014', blog_data['year'])
        self.assertEqual('01', blog_data['month'])
        self.assertEqual('03', blog_data['day'])

        