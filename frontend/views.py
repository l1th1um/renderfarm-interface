from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .forms.register import ProfileForm, UserForm
from . import utils
from django.contrib import messages


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
	context = {'title_page' : 'Login'}
	return render(request, 'frontend/login.html', context = context)

def contact(request):
	context = {'title_page' : 'Kontak'}
	return render(request, 'frontend/contact.html', context = context)


def about_us(request):
	context = {'title_page' : 'Tentang Kami'}
	return render(request, 'frontend/about_us.html', context = context)


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