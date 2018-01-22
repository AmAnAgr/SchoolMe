from django.db import models

# Create your models here.

class Feedback(models.Model):
	user_email = models.EmailField()
	