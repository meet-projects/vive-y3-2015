from django.shortcuts import render

# Create your views here.
def search_tutors(request):
	return render(request, 'app/search_tutors.html', {})
def home(request):
	return render(request, 'app/home.html', {})
def base(request):
	return render(request, 'app/after_login_base.html', {})
def profile(request):
	return render(request, 'app/profile.html', {})
def aboutusfun(request):
	return render(request, 'app/aboutus.html', {})