from django.shortcuts import render
from .models import Section, Post

# Create your views here.
def home_view(request):
	sections = Section.objects.all()
	posts = Post.objects.all()

	context = {
		'nbar' : 'home',
		'sections' : sections,
		'posts' : posts,
	}	




	return render(request, "blog.html", context)