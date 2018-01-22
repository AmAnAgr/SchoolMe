from django.db import models

# Create your models here.

class User(models.Model):
	email = models.EmailField()

	def __str__(self):
		return self.email


class School(models.Model):
	name = models.CharField(max_length=100)
	city = models.CharField(max_length=30)
	state = models.CharField(max_length=30)
	zip_code = models.IntegerField()

	def __str__(self):
		return self.name

class Feedback(models.Model):
	user_email = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
	)
	school = models.ForeignKey(
		School,
		on_delete=models.CASCADE
	)
	description = models.TextField()
	
	def __str__(self):
		return self.user_email
