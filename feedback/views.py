from django.shortcuts import render

# Create your views here.
def feedback_view(request):


	context = {
		'nbar' : 'feedback',
	}

	return render(request, 'feedback.html', context)
