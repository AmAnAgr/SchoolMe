from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers


import json


from .models import School, User, Feedback

# Create your views here.
def feedback_view(request):

	schools = School.objects.all()
	context = {
		'nbar' : 'feedback',
		'schools':schools,
	}

	return render(request, 'feedback.html', context)

def school_search(request):

	query = json.loads(request.body.decode('utf-8'))['q_school']
	schools = School.objects.filter(name__icontains=query)[:5]
	schools = serializers.serialize('json', schools)
	return HttpResponse(schools, content_type='application/json')



def save_feedback(request):
	try:
		Feedback(school=School.objects.get(pk=request.POST.get('pk')),description=request.POST.get('feedback')).save()
		success = True
	except:
		success = False

	schools = School.objects.all()
	context = {
		'nbar' : 'feedback',
		'schools':schools,
		'success' : success,
	}


	return render(request, 'feedback.html', context)


def get_feedback(request):
	feedbacks = Feedback.objects.filter(school=School.objects.get(pk=request.GET.get('qpk')))[:10]
	feedbacks = serializers.serialize('json', feedbacks)
	return HttpResponse(feedbacks)