from django.db import models
from access.models import User

# Create your models here.

class Post(models.Model):
    
    title = models.CharField(max_length=250, unique=True, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=False, null=False)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    # def summary(self):
    #     return self.content[:50]
    
    def pub_date_pretty(self):
        return self.created_on.strftime('%b %e, %Y')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=100)
    create = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['-create']


    def __str__(self):
        return 'Comment {} by {}'.format(self.body ,self.user)
    
