from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=25)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def pub_date_simple(self):
        return self.pub_date.strftime('%b %e %Y')

    def body_short(self):
        return self.body[:30]
