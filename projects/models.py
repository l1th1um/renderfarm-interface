from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import uuid


class Project(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	STATUS_LIST = (
					(0, 'Pending'),
					(1, 'Project Validation')
		)

	project_uuid = models.UUIDField(default=uuid.uuid4)
	url = models.CharField(max_length=250, blank=True)
	description = models.TextField(max_length=500)
	original_filename = models.CharField(max_length=250, blank=True)
	project_file = models.FileField(upload_to='static/uploads/project_file/',validators=[FileExtensionValidator(['zip'])], blank=True)
	status = models.SmallIntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)