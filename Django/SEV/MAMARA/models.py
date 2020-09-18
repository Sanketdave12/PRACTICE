from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Branch(models.Model):
    name= models.CharField(max_length=50)
    hod= models.CharField(max_length=100)

    def __str__(self):
        return "%s (%s)" % (self.name,self.hod)

class notice(models.Model):
    name = models.CharField(max_length=100)
    msg = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(null=True,blank=True)
    branch = models.ForeignKey(to= Branch , on_delete= CASCADE , null=True , blank=True)

class Profile(models.Model):
    user = models.OneToOneField(to=User,on_delete=CASCADE)
    branch = models.ForeignKey(to= Branch , on_delete= CASCADE , null=True , blank=True)
    def __str__(self):
        return "%s (%s)" % (self.user.username,self.branch)  