from django.db import models

# Create your models here.
class notice(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateTimeField(null=True,auto_now_add=True)
    msg  = models.TextField(null=True)