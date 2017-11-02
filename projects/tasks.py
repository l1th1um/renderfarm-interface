import logging
from subprocess import Popen, PIPE, STDOUT, run
from django.contrib.auth.hashers import make_password
from frontend import utils
from celery.decorators import task
from celery.utils.log import get_task_logger
from .models import Project

logger = get_task_logger(__name__)


@task(name='render_blender')
def render_blender(project_id, username):

	try:
		project = Project.objects.get(id=project_id)

		str_file = project.project_file.name

		#filename = str_file[-1]

		filename = str_file

		logger.info(filename)
		logging.info(filename)


		project_path = "/home/" + username + "/project" + str(project_id) + "/"

		cmd = ['mkdir', project_path]
		run(cmd)

		cmd = ['mv', project.project_file, project_path]
		run(cmd)

		cmd = ['unzip', project_path + filename]
		run(cmd)
		
		# p = Popen(cmd, stdout=PIPE, stderr=PIPE)
		# output = p.stdout.readlines()
		#
		# try :
		# 	con_msg = output[-1].decode("utf-8").split(' ')
		# 	password = con_msg[2]
		# 	hashed_password = make_password(password)
		# 	user.password = hashed_password
		# 	user.is_active = 1
		# 	user.save()
		#
		# 	message = message_success_activate(user, password)
		# 	subject = "Welcome to RenderFarm LIPI"
		#
		# 	utils.send_mail(user.email, subject, message)
		# except IndexError:
		# 	pass
	except Project.DoesNotExist:
		logging.warning("Project '%s' Does Not Exist" % project_id)

def message_success_activate(user, password):
	message = ("Hello {name}, \n\n" +
				"You have a new RenderFarm account at http://render.grid.lipi.go.id \n\n" +
				"Your username: {username}\n\n" +
				"Your password: {password}\n\n\n\n\n" +
				"RenderFarm Administrator")

	return message.format(name=user.first_name, username=user.username, password=password)
