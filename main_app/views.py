from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .helper import admin_template
from django.core import urlresolvers
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test

def index(request):
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
	return render(request, 'frontend/index.html', context=context_dict)

def register(request):
	return render(request, 'register.html')

def login(request):
	return HttpResponse("<h1>Login" +  admin_template() +"</h1>")

@login_required()
@user_passes_test(lambda u: u.is_superuser)
def home(request):
	return render(request, 'main_app/home.html')

def urls(request):
	patterns = _get_named_patterns()
	r = HttpResponse(intro_text, content_type = 'text/plain')
	longest = max([len(pair[0]) for pair in patterns])
	for key, value in patterns:
		r.write('%s %s\n' % (key.ljust(longest + 1), value))
	return r

def _get_named_patterns():
	"Returns list of (pattern-name, pattern) tuples"
	resolver = urlresolvers.get_resolver(None)
	patterns = sorted([
		(key, value[0][0][0])
		for key, value in resolver.reverse_dict.items()
		if isinstance(key, str)
	])
	return patterns