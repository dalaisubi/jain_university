from django.db import models
from django.contrib.auth.models import User


class FileUpload(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    datafile = models.FileField()


class File(models.Model):
	file = models.FileField(blank=False, null=False)
	remark = models.CharField(max_length=20)
	owner = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE, default=1)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.remark