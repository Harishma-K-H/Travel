from django.db import models
class place(models.Model):
    des=models.TextField()
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='gallery')
# Create your models here.
class teams(models.Model):
    img=models.ImageField(upload_to='pic')
    membername=models.CharField(max_length=300)
    memberdes=models.TextField()


    def __str__(self):
        return self.membername
