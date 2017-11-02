import logging
 
from django.contrib.auth import get_user_model
#from djrenderfarm.celery import app
from subprocess import Popen, PIPE, STDOUT
from django.contrib.auth.hashers import make_password
from frontend import utils
from celery.decorators import task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@task(name='create_user_bash')
def create_user_bash(user_id):
	print(" Step 4 ")
	logging.info("Goes Here")
	logger.info("Goes Here")
	UserModel = get_user_model()
	print("It Goes Here")
	try:
		user = UserModel.objects.get(pk=user_id)

		cmd = ['ssh', 'root@192.168.222.3', "/root/bin/create-render-user.sh /root/conf/tauke02.hosts " + user.username + " 1004 "]
		
		p = Popen(cmd, stdout=PIPE, stderr=PIPE)
		output = p.stdout.readlines()
		print(" Step 5 ")
		try :
			print(" Step 6 ")
			con_msg = output[-1].decode("utf-8").split(' ')
			password = con_msg[2]
			hashed_password = make_password(password)
			user.password = hashed_password
			user.is_active = 1
			user.save()

			message = message_success_activate(user, password)
			subject = "Welcome to RenderFarm LIPI"

			utils.send_mail(user.email, subject, message)
		except IndexError:
			pass
	except UserModel.DoesNotExist:
		logging.warning("User '%s' Does Not Exist" % user_id)

def message_success_activate(user, password):
	message = ("Hello {name}, \n\n" +
				"You have a new RenderFarm account at http://render.grid.lipi.go.id \n\n" +
				"Your username: {username}\n\n" +
				"Your password: {password}\n\n\n\n\n" +
				"RenderFarm Administrator")

	return message.format(name=user.first_name, username=user.username, password=password)
