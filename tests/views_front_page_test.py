from base_test_handler import TestHandler 

class FrontPageTest(TestHandler):
    '''
    test the of the website
    '''

    def test_front_page_get_response(self):
        '''
        test that the front page responds to a normal get request at '/'
        '''
        response = self.testapp.get('/')
        self.assertEqual(response.status_int, 200)