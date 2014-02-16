from controllers.discover_blog_files import discover_blog_files
from base_test_handler import TestHandler


class DiscoverBlogFilesTest(TestHandler):
    '''
    test the the controller for discovering all the blog files in the blog files directory
    '''

    def test_discover_blog_files_function(self):
        '''
        fetching the blog map should return something that is not none!
        '''
        file_list = discover_blog_files()
        self.assertIsNotNone(file_list)
        self.assertEqual(len(file_list), 11)

        