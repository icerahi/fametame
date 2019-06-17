from django.contrib import admin

# Register your models here.
from photos.models import Photo,Comment

admin.site.register(Photo)
admin.site.register(Comment)