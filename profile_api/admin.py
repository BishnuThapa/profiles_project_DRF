from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(UserAdmin):
    list_display = ('email', 'name',
                    'is_active')
    list_display_links = ('email', 'name',)
    ordering = ('-email',)
    filter_horizontal = ()
    fieldsets = ()
    list_filter = ()


admin.site.register(ProfileFeedItem)