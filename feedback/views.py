from django.shortcuts import render

from .models import School, User, Feedback

# Create your views here.
def feedback_view(request):

	schools = School.objects.all()
	context = {
		'nbar' : 'feedback',
		'schools':schools,
	}

	return render(request, 'feedback.html', context)

def feedback_new_submit(request):
	
	schools = School.objects.all()
	context = {
		'nbar' : 'feedback',
		'schools':schools,
	}

	return render(request, 'feedback.html', context)

def feedback_existing_submit(request):

	schools = School.objects.all()
	context = {
		'nbar' : 'feedback',
		'schools':schools,
	}

	return render(request, 'feedback.html', context)