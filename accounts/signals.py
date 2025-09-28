from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

@receiver(post_save, sender=User)
def add_user_to_buyers(sender, instance, created, **kwargs):
    if created:
        buyer_group, _ = Group.objects.get_or_create(name="Buyer")
        instance.groups.add(buyer_group)