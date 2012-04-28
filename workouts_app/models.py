from django.db import models

class User(models.Model):
	name = models.CharField(max_length=100)
	def __unicode__(self):
		return self.name
class Workout(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=100)
	desc = models.CharField(max_length=300)
	def __unicode__(self):
		return self.name+", "+self.user.name

class Exercise(models.Model):
	workout = models.ForeignKey(Workout)
	name = models.CharField(max_length=100)
	durorreps = models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.name+", "+ self.durorreps
