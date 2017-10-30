from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from .forms.register import ProfileForm, UserForm
from . import utils
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as frontend_login
from projects.forms.user_project import ProjectForm
from django.contrib.auth.decorators import login_required
from projects.models import Project

def index(request):
	context = {'title_page' : 'Home'}
	return render(request, 'frontend/home.html', context = context)

@require_http_methods(["GET", "POST"])
def register(request):
	context = {'title_page': 'Registrasi'}

	if request.method == 'POST':
		user_form = UserForm(request.POST)
		profile_form = ProfileForm(request.POST, request.FILES)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save(commit=False)
			user.username = utils.generate_username(request.POST['first_name'])
			user.is_active = 0
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()

			messages.success(request, 'User has been registered')
			return redirect('/register')
		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = ProfileForm()

	context['user_form'] = user_form
	context['profile_form'] = profile_form

	return render(request, 'frontend/register.html', context = context)

def login(request):
	if request.user.is_active:
		return redirect('/profile')

	context = {'title_page' : 'Login'}
	if request.method == 'POST':
		member_login(request)
	return render(request, 'frontend/login.html', context = context)

def member_login(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			frontend_login(request, user)
			return redirect('/project_monitoring')
	else :
		messages.success(request, 'Invalid Username or Password')
		return redirect('/login')

def contact(request):
	context = {'title_page' : 'Kontak'}
	return render(request, 'frontend/contact.html', context = context)


def about_us(request):
	context = {'title_page' : 'Tentang Kami'}
	return render(request, 'frontend/about_us.html', context = context)

@login_required(login_url='/login/')
def project_monitoring(request):
	context = {'title_page' : 'Project Monitoring'}

	projects = Project.objects.filter(user_id=request.user.id)

	context['projects'] = projects

	if request.method == 'POST':
		project_form = ProjectForm(request.POST, request.FILES)

		if project_form.is_valid() :
			project = project_form.save(commit=False)
			project.user_id = request.user.id
			project.original_filename = request.FILES['project_file'].name
			project.save()

			messages.success(request, 'Project has been uploaded. Waiting for Administrator Approval')
			return redirect('/project_monitoring')
		else:
			print(project_form.errors)

	else:
		project_form = ProjectForm()

	context['project_form'] = project_form

	return render(request, 'frontend/project_monitoring.html', context = context)

def under_construction(request):
	context = {'title_page' : 'Sedang Dalam Pengembangan'}
	return render(request, 'frontend/under_construction.html', context = context)

def profile(request):
	context = {'title_page' : 'Profile'}
	return render(request, 'frontend/profile.html', context = context)

def services(request):
	context = {'title_page' : 'Service'}
	return render(request, 'frontend/services.html', context = context)

def policy(request):
	context = {'title_page' : 'Policy'}
	return render(request, 'frontend/policy.html', context = context)

def news(request):
	context = {'title_page' : 'Berita'}
	return render(request, 'frontend/news.html', context = context)

def terms(request):
	context = {'title_page' : 'Terms'}
	return render(request, 'frontend/terms.html', context = context)