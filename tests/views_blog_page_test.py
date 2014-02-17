from base_test_handler import TestHandler 

class BlogPageTest(TestHandler):
    '''
    test the front page of the blog app
    '''

    def test_blog_page_get_request(self):
        '''
        test that the blog page responds to a normal get request at '/blog'
        '''
        response = self.testapp.get('/blog')
        self.assertEqual(response.status_int, 200)