from django.conf import settings
from django.db import models

# Create your models here.
from django.urls import reverse

 



class Photo(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='photo/',blank=False,null=False)
    caption=models.CharField(max_length=5000,null=True,blank=True)
    liked =models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='liked')
    posted_on=models.DateTimeField(auto_now_add=True)
    timestamp=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return (self.caption)

    class Meta:
        ordering=['-timestamp']

    def get_absolute_url(self):
        return reverse('photo:detail',kwargs={"pk":self.pk})

    def get_delete_url(self):
        return reverse('photo:delete',kwargs={"pk":self.pk})

    def get_update_url(self):
        return reverse('photo:update',kwargs={'pk':self.pk})


class Comment(models.Model):
    photo=models.ForeignKey(Photo,on_delete=models.CASCADE,related_name='commented_photo')
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='comment_user')
    comment=models.TextField(max_length=160,null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.photo.caption,str(self.user.username))
