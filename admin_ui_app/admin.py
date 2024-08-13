# Register your models here.
from django.contrib import admin
from .models import Excel_files_model
from django.contrib.auth.models import User, Group



class CustomAdminSite(admin.AdminSite):
    site_header = "My Custom Admin"
    site_title = "My Admin Portal"
    index_title = "Welcome to My Admin"

custom_admin_site = CustomAdminSite(name='custom_admin')



custom_admin_site.register(User)


# @admin.register(Excel_files_model, site=my_admin_site)
# class a(admin.ModelAdmin):
#     list_display = ('title', 'author', 'published_date', 'isbn')

# # In urls.py, you will link to this custom admin site