from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import MasterPassword


@receiver(post_save, sender=User)
def createMasterPassword(sender, instance, created, **kwargs):
    if created:
        MasterPassword.objects.create(author=instance)


@receiver(post_save, sender=User)
def saveMasterPassword(sender, instance, created, **kwargs):
    # if created == False:
    instance.masterpassword.save()
