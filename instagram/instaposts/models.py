from django.db import models
from instausers.models import Profile, UserAccount
from cloudinary.models import CloudinaryField
from django.urls import reverse


# Create your models here.

class InstaPosts(models.Model):
    author = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    body = models.TextField()
    likes = models.ManyToManyField(UserAccount, default=None, blank=True, related_name='likes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.body)

    def get_absolute_url(self):
        return reverse('profile')

    @property
    def number_of_likes(self):
        return self.likes.all().count()

    class Meta:
        ordering = ('-created',)

LIKE_CHOICES = [
    ('like', 'like'),
    ('unlike', 'unlike'),
]

class Like(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    post = models.ForeignKey(InstaPosts, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='like', max_length=10)

    def __str__(self):
        return str(self.post)