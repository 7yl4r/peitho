

# get content from reddit
from py.actions.getContent.reddit import redditContentInterface as contentInterface
from py.actions.postContent.Facebook import facebookPoster as postInterface

content_interface = contentInterface()
ctnt = content_interface.findInterestingContent()



# do something with it 
print '\nselected post from reddit:'
print ctnt.text
print ctnt.link

print '\n posting to fb...'
poster = postInterface()
poster.postcontent(ctnt)