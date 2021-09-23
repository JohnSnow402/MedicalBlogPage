from django.contrib import admin
from .models import AddComment, AddPost, Services
# Register your models here.

admin.site.register(AddPost)
admin.site.register(AddComment)
admin.site.register(Services)
