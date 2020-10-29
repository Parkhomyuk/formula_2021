from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from formula_app.models import userProfile

class ProfileUserInline(admin.StackedInline):
    model = userProfile
    can_delete = False
    verbose_name_plural ='profile_user'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileUserInline,)    

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
