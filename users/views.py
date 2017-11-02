from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from .tasks import create_user_bash

# Create your views here.
@login_required()
@user_passes_test(lambda u: u.is_superuser)
def index(request):
	users = User.objects.all()
	context = {'title_page' : 'User Management', 'users' : users}
	return render(request, 'users/index.html', context = context)

@login_required()
@user_passes_test(lambda u: u.is_superuser)
def edit(request, user_id):
	user = User.objects.get(id=user_id)

	if request.method == 'POST':
		print(" Step 1 ")
		try :
			print(" Step 2 ")
			create_user_bash.delay(user_id)
			print(" Step 3 ")

			messages.success(request, 'User has been activated')
			return redirect('/dashboard/users')

		except IndexError:
			pass

	context = {'title_page' : 'Edit Management', 'user' : user}
	return render(request, 'users/edit.html', context = context)

def message_success_activate(user, password):
	message = ("Hello {name}, \n\n" +
				"You have a new RenderFarm account at http://render.grid.lipi.go.id \n\n" +
				"Your username: {username}\n\n" +
				"Your password: {password}\n\n\n\n\n" +
				"RenderFarm Administrator")

	return message.format(name=user.first_name, username=user.username, password=password)