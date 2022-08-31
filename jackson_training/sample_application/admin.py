from django.contrib import admin

# Register your models here.
from .models import *


# display list of data

class BlogAdmin(admin.ModelAdmin):
    # add all the fiels here to be shown in the admin
    list_display = ('title','published')


admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Blog,BlogAdmin)