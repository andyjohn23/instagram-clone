from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from PIL import Image

# Create your models here.

class ManagerAccount(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('users must have an emailaddress')
        if not username:
            raise ValueError('users must have a username')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )

        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=70, unique=True)
    username = models.CharField(max_length=70, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = ManagerAccount()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Profile(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    image = models.ImageField(default='default-avatar.jpg', upload_to='profile_pics')
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    followers = models.ManyToManyField(UserAccount, blank=True, related_name='followers')

    def profile_instaposts(self):
        return self.instaposts_set.all()

    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ('-date_joined',)




    
