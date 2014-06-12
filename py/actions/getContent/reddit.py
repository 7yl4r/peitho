
from py.GLOBALS import USER_AGENT
from py.Content import Content

import praw

class redditContentInterface(object):

    def __init__(self):
        self.reddit = praw.Reddit(user_agent=USER_AGENT)
       # self.reddit.login()

    def findInterestingContent(self):
        self.selectedContent = Content( redditPost=self.selectBest(self.getSelection()) )
        return self.selectedContent

    ### private methods? ###

    def getSelection(self):
        '''
        Returns a selection of reddit posts using bot prefs
        '''
        sub = self.reddit.get_subreddit('technology')
        posts = sub.get_hot(limit=10)
        return posts

    def selectBest(self, posts):
        '''
        selects the best post in the list given
        '''
        # TODO: do something more clever here
        return next(posts)
