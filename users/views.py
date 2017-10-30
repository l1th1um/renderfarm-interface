from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from subprocess import Popen, PIPE, STDOUT


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
		cmd = 'ssh root@192.168.222.3 "/root/bin/create-render-user.sh conf/tauke02.hosts ' + user.username + ' 1004 "'
		#p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
		#output = p.stdout.read()
		p = Popen(cmd, stdout=PIPE, stderr=PIPE)
		#stdout, stderr = p.communicate()
		output = p.stdout.readlines()
		
		print("Oucchhh.....")
		print(output[-1])

	context = {'title_page' : 'Edit Management', 'user' : user}
	return render(request, 'users/edit.html', context = context)