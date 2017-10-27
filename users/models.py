from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	address = models.TextField(max_length=500, blank=True)
	phone = models.CharField(max_length=30)
	#birth_date = models.DateField(null=True, blank=True)
	office_phone = models.CharField(max_length=30)
	institution = models.CharField(max_length=150)
	job_title = models.CharField(max_length=30)
	resident_id = models.CharField(max_length=50)
	resident_file = models.ImageField(upload_to='uploads/resident_file/', blank=True)

	'''
	def __str__(self):
		return self.user.username
	
	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()
	'''