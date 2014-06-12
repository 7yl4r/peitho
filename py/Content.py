'''
defines the Content class which describes a piece of content in its entirety
'''

__author__ = '7yl4r'

class Content(object):
    def __init__(self, redditPost=None):
        if redditPost is not None:
            self.text = redditPost.title
            self.link = redditPost.url

            self.img = None  # TODO: check if link is or has img?
            self.mood = None  # TODO: add mood?

        else :
            self.text = ''
            self.img  = None
            self.link = None
            self.mood = None