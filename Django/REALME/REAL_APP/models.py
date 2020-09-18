from django.db import models

# Create your models here.
class sd(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    msg = models.TextField()
    date = models.DateTimeField(auto_now_add=True)