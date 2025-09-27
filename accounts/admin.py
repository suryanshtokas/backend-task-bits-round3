from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AdminUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = AdminUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser 
    list_display = [
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets

admin.site.register(CustomUser, CustomUserAdmin)
