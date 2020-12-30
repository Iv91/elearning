from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from .models import Author
from django.contrib.auth.models import Group

User = get_user_model()

def author_profile(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(
        user=instance,
        )
post_save.connect(author_profile, sender=User)
