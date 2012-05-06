from django.db import models
from django.contrib.auth import models as authmods

class User(authmods.User):
	is_staff = False
	def __unicode__(self):
		return self.get_full_name()

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
