from django.shortcuts import render
from .models import Class, Subject

# Create your views here.
def study_material_view(request, class_no=0):
	if( class_no != 0 ):
		subjects = list(Subject.objects.filter(of_class=Class.objects.get(class_number=class_no)))
	else:
		subjects = None
	
	classes = Class.objects.all()

	context = {
		'nbar' : 'study_material',
		'subjects' : subjects,
		'classes' : classes,

	}

	return render(request, 'study_material.html', context)
