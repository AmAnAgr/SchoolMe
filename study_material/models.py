from django.db import models

# Create your models here.
class Class(models.Model):
	class_number = models.IntegerField()

	def __str__(self):
		return "Class " + str(self.class_number)

class Link(models.Model):
	url = models.URLField()
	description = models.TextField()

	def __str__(self):
		return self.description




class Subject(models.Model):
	title = models.CharField(max_length=30)
	of_class = models.ForeignKey(
		Class,
		on_delete=models.CASCADE,
	)
	links = models.ManyToManyField(Link)

	def __str__(self):
		return self.title
