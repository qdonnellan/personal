from base_test_handler import TestHandler 

class BlogPageTest(TestHandler):
    '''
    test the of the website
    '''

    def test_blog_page_get_request(self):
        '''
        test that the blgo page responds to a normal get request at '/'
        '''
        response = self.testapp.get('/blog')
        self.assertEqual(response.status_int, 200)