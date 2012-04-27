# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from workouts_app.models import *


def userhome(request, uid):
	u = get_object_or_404(User, pk=uid)
	return render_to_response('workouts/user.html', {'user':u})

def home(request):
	return render_to_response('workouts/index_temp.html')	

def wkdetail(request, uid, wkoutname):
	u = get_object_or_404(User, pk=uid)
	w = get_object_or_404(Workout,user=u , name=wkoutname)
	d = []
	return render_to_response('workouts/wkoutdetail.html', {'workout':w, })
