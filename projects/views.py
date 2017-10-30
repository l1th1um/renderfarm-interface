from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from subprocess import Popen, PIPE, STDOUT
from django.contrib.auth.hashers import make_password
from frontend import utils
from django.contrib import messages
from projects.models import Project

# Create your views here.
@login_required()
@user_passes_test(lambda u: u.is_superuser)
def index(request):
	projects = Project.objects.all()
	context = {'title_page' : 'Project Management', 'projects' : projects}
	return render(request, 'projects/index.html', context = context)

@login_required()
@user_passes_test(lambda u: u.is_superuser)
def edit(request, user_id):
	user = User.objects.get(id=user_id)

	if request.method == 'POST':
		cmd = ['ssh', 'root@192.168.222.3', "/root/bin/create-render-user.sh /root/conf/tauke02.hosts " + user.username + " 1004 "]
		
		p = Popen(cmd, stdout=PIPE, stderr=PIPE)
		output = p.stdout.readlines()
		

		try :
			con_msg = output[-1].decode("utf-8").split(' ')
			password = con_msg[2]
			hashed_password = make_password(password)
			user.password = hashed_password
			user.is_active = 1
			user.save()

			message = message_success_activate(user, password)
			subject = "Welcome to RenderFarm LIPI"

			utils.send_mail(user.email, subject, message)

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