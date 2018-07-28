from mongoengine import *

class Post(Document):
    title = StringField()
    author = StringField()
    content = StringField()
    
import mlab
mlab.connect()
# create new post
post_hobby = Post(title = 'hello c4t4',author = 'Nguyên',content = 'no comment')

post_hobby.save()

