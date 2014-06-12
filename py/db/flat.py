'''
defines access to "database" hard-coded into this file.
'''

def getSubredditByContentDescriptor(desc):
    '''
    returns subreddit which best matches the descriptor given.
    '''
    if desc == 'funny':
        return '/r/funny'
