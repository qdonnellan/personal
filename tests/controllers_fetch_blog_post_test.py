from controllers.fetch_blog_post import fetch_blog_post
from base_test_handler import TestHandler

class FetchBlogPostTest(TestHandler):
    '''
    test the controller for fetching a blog post
    '''

    def test_fetch_for_non_existing_blog_post(self):
        '''
        test that a bad blog post id returns None
        '''
        data = fetch_blog_post('2077', '12', '04')
        self.assertIsNone(data)
        
    def test_fetch_for_existing_blog_post(self):
        '''
        test that a request for an existing blog post returns that post
        '''
        data = fetch_blog_post('2013', '03', '27')
        self.assertIsNotNone(data)

