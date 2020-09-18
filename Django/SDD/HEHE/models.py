from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator , MaxValueValidator ,RegexValidator

# Create your models here.
class Branch(models.Model):
    name= models.CharField(max_length=50)
    hod= models.CharField(max_length=100)

    def __str__(self):
        return "%s (%s)" % (self.name,self.hod)

class Notice(models.Model):
    name = models.CharField(max_length=100)
    msg = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(null=True,blank=True)
    branch = models.ForeignKey(to= Branch , on_delete= CASCADE , null=True , blank=True)

class Profile(models.Model):
    user = models.OneToOneField(to=User,on_delete=CASCADE)
    branch = models.ForeignKey(to= Branch , on_delete= CASCADE , null=True , blank=True)
    sem = models.IntegerField(default=1, choices=((1,1),(2,2),(3,3),(4,4),(5,5),(6,6)))
    marks_10 = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(100)])
    marks_12 = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(100)])
    marks_aggr = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(100)])
    Phone = models.CharField(max_length=10,validators=[RegexValidator('0?[5-9]{1}\d{9}$')],null =True,blank = True)
    myimg = models.ImageField(upload_to="images\\" , null =True)

    def __str__(self):
        return "%s (%s)" % (self.user.username,self.branch)  