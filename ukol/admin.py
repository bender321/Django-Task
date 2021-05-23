from django.contrib import admin
from .models import Entrepreneur

#Disable option to create records in Django admin site
class MyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(Entrepreneur, MyAdmin)

