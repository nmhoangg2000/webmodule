import mlab
from models.user import User
from models.post import Post
mlab.connect()
# a_random_user = User.objects(username="hoang").first()
# if a_random_user is None:
#     print("user not found")
# else:
#     new_post = Post(title="Bai viet so 2 cua Hoang",
#                     content="Hoang dep trai",
#                     owner=a_random_user)  
# new_post.save()
# print("Done saving...")                    


#post => owner
# for post in Post.objects():
#     print(post.title,"by", post.owner.username)
    
# owner => posts
user = User.objects(username="hoang").first()
print("Posts owned by", user.username,":")
posts = Post.objects(owner=user)
for post in posts:
    print(post.title)
