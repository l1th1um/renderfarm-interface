'''
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receive

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #bio = models.TextField(max_length=500, blank=True)
    #location = models.CharField(max_length=30, blank=True)
    #birth_date = models.DateField(null=True, blank=True)

    address = models.TextField()
    phone = models.CharField(max_length=30)
    office_phone = models.CharField(max_length=30)
    institution = models.CharField(max_length=150)
    job_title = models.CharField(max_length=30)
    resident_id = models.CharField(max_length=50, label='Residential No/Passport No')
    resident_file = models.FileField(upload_to='uploads/')
    accept = models.BooleanField(error_messages={'required' : 'Please Accept Terms and Condition Before Using Our Service'})

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''