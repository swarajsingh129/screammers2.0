from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(upload_to="user_image", blank=True, null=True)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username + " " + str(self.date) 

