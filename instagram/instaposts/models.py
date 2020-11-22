from django.db import models
from instausers.models import Profile

# Create your models here.

class InstaPosts(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.body)[:30]

    class Meta:
        ordering = ('-created',)


