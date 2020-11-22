from django.contrib import admin
from instausers.models import UserAccount,Profile

# Register your models here.
admin.site.register(UserAccount)
admin.site.register(Profile)