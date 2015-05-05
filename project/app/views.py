from django.shortcuts import render
from app.models import Accounts
# Create your views here.
def search_tutors(request):
	return render(request, 'app/search_tutors.html', {})
def home(request):
	email = request.POST["email"]
	password = request.POST["password"]

	user = Accounts.objects.filter(email = email, password = password)
	if len(user) == 1:
		return render(request, 'app/home.html', {})
	else:
		return render(request, 'app/index.html', {})
def base(request):
	return render(request, 'app/after_login_base.html', {})
def profile(request):
	return render(request, 'app/profile.html', {})
def aboutusfun(request):
	return render(request, 'app/aboutus.html', {})
def register(request):
	email = request.POST["email"]
	password = request.POST["password"]

	tempUser = Accounts.objects.filter(email = email, password = password)
	if len(tempUser)==0:
		user = Accounts(email = email, password = password)
		user.save()
	return render(request, 'app/index.html', {})
