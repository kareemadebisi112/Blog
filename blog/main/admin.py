from django.contrib import admin
from main.models import *

admin.site.register(Visitor)
admin.site.register(Email)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(PostCategory)
admin.site.register(PostTag)