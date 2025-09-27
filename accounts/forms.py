from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm
from django.contrib.auth.models import Group

from .models import CustomUser


class CustomAdminUserCreationForm(AdminUserCreationForm):
    class Meta(AdminUserCreationForm):
        model = CustomUser
        fields = AdminUserCreationForm.Meta.fields

    def save(self, commit=True):
        user = super().save(commit)
        if commit:
            buyer_group = Group.objects.get(name="Buyer")
            user.groups.add(buyer_group)
        return user


class CustomUserChangeForm(UserChangeForm):     
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields