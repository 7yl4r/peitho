__author__ = '7yl4r'

import facebook

APP_ID = '533629643408777'
REDIRECT_URI = 'https://www.facebook.com/connect/login_success.html'

class facebookPoster(object):

    def __init__(self):
        # TODO: token needs to be retrieved, not hard-coded
        login = ('https://www.facebook.com/dialog/oauth?'
                 + 'client_id=' + APP_ID
                 + '&redirect_uri=' + REDIRECT_URI)
        self.token = ''
        self.graph = facebook.GraphAPI(self.token)

    def postcontent(self, content):
        #profile = self.graph.get_object("me")
        #friends = self.graph.get_connections("me", "friends")
        self.graph.put_object("me", "feed", message="Test post; please do not read.") # message=content.text)
