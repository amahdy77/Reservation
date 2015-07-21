from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import string, random

# Create your models here.

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class ExpectedUser(models.Model):
    fullname = models.CharField(blank=False, null=False, max_length=120)
    guests = models.IntegerField(blank=False, null=False, default=1)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_modified = models.DateTimeField(auto_now_add=False, auto_now=True)
    registration = models.CharField(max_length=16, blank=True, editable=False, unique=True)


    def __unicode__(self):
        return self.fullname


@receiver(post_save, sender=ExpectedUser)
def add_registration_id_to_model(sender, instance, *args, **kwargs):
    sender.objects.filter(pk=instance.pk).update(registration=id_generator())


