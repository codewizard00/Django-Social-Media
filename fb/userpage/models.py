from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,null=True)
    desc = models.CharField(max_length=50,null=True)
    image = models.ImageField(upload_to="post",null=True)
    post_date = models.DateTimeField(auto_now_add=True,)
    

class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE,null=True)
    user_image = models.ImageField(upload_to ="user_image",null=True)
    bio = models.CharField(max_length=200,null=True)
    connection = models.CharField(max_length=200, null=True)
    follower = models.IntegerField(default=0)
    following = models.IntegerField(default=0)


class Following(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    followed = models.ManyToManyField(User , related_name="followed")
    
    @classmethod
    def follow(cls,user , another_account):
        obj , create = cls.get_or_create(user=user)
        obj.followed.add(another_account)
        print("unfollowed")

    @classmethod
    def unfollow(cls,user,another_account):
        obj , create = cls.get_or_create(user=user)
        obj.followed.remove(another_account)
        print("unfollowed")
