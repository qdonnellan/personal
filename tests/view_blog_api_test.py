from base_test_handler import TestHandler 
import json

class BlogAPITest(TestHandler):
    '''
    test that the blog api is operational
    '''

    def test_get_request_for_known_blog_post(self):
        '''
        test that the request '/api/blog/2014/01/03' returns a useful json objects with
        expected properties
        '''
        response = self.testapp.get('/api/blog/2014/01/03')
        self.assertEqual(response.status_int, 200)


        blog_data = json.loads(response.body)
        self.assertEqual("10 Posts in 10 Days", blog_data['title'])
        self.assertEqual('2014', blog_data['year'])
        self.assertEqual('01', blog_data['month'])
        self.assertEqual('03', blog_data['day'])

    def test_get_latest_blog_post(self):
        '''
        a call to '/api/blog/latest' should return the latest blog post
        '''
        response = self.testapp.get('/api/blog/latest')
        self.assertEqual(response.status_int, 200)
        blog_data = json.loads(response.body)
        self.assertEqual("We're Published!", blog_data['title'])

    def test_get_blog_map(self):
        '''
        a call to '/api/blog/map' should return blog map in json format
        '''
        response = self.testapp.get('/api/blog/2014/01/03')
        self.assertEqual(response.status_int, 200)

