from django import forms
from workouts_app.models import *

class NewWorkout(forms.Form):
    wkout_name = CharField(max_length = 100)
    wkout_desc = CharField(max_length = 300)

