from django.contrib import admin
from . models import Follower, Posts, Comments, Profile_photo

# Register your models here.
admin.site.register(Follower)
admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(Profile_photo)
