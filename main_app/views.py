from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .helper import admin_template
from django.core import urlresolvers
from django.http import HttpResponse

intro_text = """Named URL patterns for the {% url %} tag
========================================

e.g. {% url pattern-name %}
or   {% url pattern-name arg1 %} if the pattern requires arguments

"""


def index(request):
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
	return render(request, 'frontend/index.html', context=context_dict)


def register(request):
	return render(request, 'register.html')

def login(request):
	return HttpResponse("<h1>Login" +  admin_template() +"</h1>")

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