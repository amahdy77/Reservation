from django.db import models, IntegrityError
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


    def save(self, *args, **kwargs):
        if not self.registration:
            self.registration = id_generator()
            # using your function as above or anything else
        success = False
        failures = 0
        while not success:
            try:
                super(ExpectedUser, self).save(*args, **kwargs)
            except IntegrityError:
                failures += 1
                if failures > 5:  # or some other arbitrary cutoff point at which things are clearly wrong
                    raise
                else:
                    # looks like a collision, try another random value
                    self.registration = id_generator()
            else:
                success = True


    def __unicode__(self):
        return self.fullname