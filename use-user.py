import post
import user

app_user_one = user.User("somebody@gmail.com", "Somebody", "abc123", "DevOps Engineer")
app_user_one.get_user_info()

app_user_two = user.User("nobody@gmail.com", "Nobody", "def456", "Software Engineer")
app_user_two.get_user_info()

new_post = post.Post("on a secret mission today", app_user_two.name)
new_post.get_post_info()
