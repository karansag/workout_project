# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from workouts_app.models import *
from django.template import RequestContext
import random


def userhome(request, uid):
	u = get_object_or_404(User, pk=uid)
	return render_to_response('user.html', {'user':u})

def home(request):
	return render_to_response('index_temp.html')	

def wkdetail(request, uid, wkout_num):
	u = get_object_or_404(User, pk=uid)
	w = u.workout_set.get(id=wkout_num)
	return render_to_response('wkoutdetail.html', {'workout':w })

def random_workout(request, uid):
	#get user's workouts and pick a random one
	u = get_object_or_404(User, pk=uid)
	workoutnum = u.workout_set.count()
	
	rand = random.randint(1, workoutnum)

	return wkdetail(request,uid, rand)

def addworkout(request, uid):

    thisuser = get_object_or_404(User, pk=uid)
    addworkouturl = '/u/'+uid+'/addworkout/'
    if request.method == 'POST':
        #assumes input has been cleaned...TODO: validate form
        name = request.POST['wkout_name']
        desc = request.POST['wkout_desc']

        w = Workout(user=thisuser, name=name, desc=desc)
        w.save()

        exnames = request.POST.getlist('ex_name', [])
        exreps = request.POST.getlist('ex_reps', [])
        num_ex = len(exnames)

        for i in range(num_ex):
            e = Exercise(name=exnames[i], durorreps=exreps[i], workout=w)
            e.save()

        return HttpResponseRedirect('/u/'+str(uid))
    
    return render_to_response('addworkout.html', {'user':thisuser, 'posturl':addworkouturl}
            , RequestContext(request))
