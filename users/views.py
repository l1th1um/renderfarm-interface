from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User


# Create your views here.
@login_required()
@user_passes_test(lambda u: u.is_superuser)
def index(request):
	users = User.objects.all()
	context = {'title_page' : 'User Management', 'users' : users}
	return render(request, 'users/index.html', context = context)