from main_view_handler import ViewHandler

class FrontPage(ViewHandler):
    '''
    view handler for the front page of the app
    '''
    
    def get(self):
        '''
        handle the get request
        '''
        self.render('home.html', home_active ="active")