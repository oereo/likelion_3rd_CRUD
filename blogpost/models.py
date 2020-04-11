from django.db import models

# Create your models here.

class Blog(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]

class Comment(models.Model):
    blog = models.ForeignKey('blogpost.Blog', on_delete=models.CASCADE, null=True, related_name='comments')
    #author = models.ForeignKey('blogpost.Blog', on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField('date published')
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text