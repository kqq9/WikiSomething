from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import wikiEntry
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import wikipedia

# Create your views here.

def login_view(request):
	return render(request, 'login.html')

def entry(request):
	#entry = get_object_or_404(wikiEntry, pk=wikiEntry.objects.last().id)
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		return render(request, 'test.html', {'search': entry.search, 'search_time': entry.search_date})    
	else:
		return HttpResponse('Failed To Log In')

def wiki(request):
	if request.method == 'POST':
		new_search = request.POST['index']
		# Handle request.POST['csrfmiddlewaretoken']
		wikiEntry(search=new_search, search_date=timezone.now(), ip_address=request.META['REMOTE_ADDR']).save()
		try:
			w = wikipedia.summary(new_search)
			return render(request, 'test2.html', {'arg1': new_search, 'arg2': w})
		except wikipedia.PageError:
			try:
				ww = wikipedia.search(w)
				if ww:
					return HttpResponse('No such article {}; found articles:\n{}'.format(new_search, '\n'.join(ww)))
				else:
					return HttpResponse('No such article {}; no other results found.'.format(new_search))
			except:
				return HttpResponse('No such article {}; no other results found.'.format(new_search))
		#return HttpResponse('Submitted the search {}'.format(new_search))
	elif request.method == 'GET':
		return HttpResponse('Can\'t view this page without submitting a form.')
