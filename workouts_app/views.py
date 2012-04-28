# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from workouts_app.models import *
import random

def userhome(request, uid):
	u = get_object_or_404(User, pk=uid)
	return render_to_response('workouts/user.html', {'user':u})

def home(request):
	return render_to_response('workouts/index_temp.html')	

def wkdetail(request, uid, wkout_num):
	u = get_object_or_404(User, pk=uid)
	w = u.workout_set.get(id=wkout_num)
	return render_to_response('workouts/wkoutdetail.html', {'workout':w })

def random_workout(request, uid):
	#get user's workouts and pick a random one
	u = get_object_or_404(User, pk=uid)
	workoutnum = u.workout_set.count()
	
	rand = random.randint(1, workoutnum)

	return wkdetail(request,uid, rand)
	
