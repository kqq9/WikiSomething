from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import wikiEntry
from django.utils import timezone

# Create your views here.

def index(request):
	entry = get_object_or_404(wikiEntry, pk=1)
	return render(request, 'test.html', {'search': entry.search, 'search_time': entry.search_date})

def wiki(request):
	if request.method == 'POST':
		new_search = request.POST['index']
		# Handle request.POST['csrfmiddlewaretoken']
		wikiEntry(search=new_search, search_date=timezone.now()).save()
		return HttpResponse('Submitted the search {}'.format(new_search))
	elif request.method == 'GET':
		return HttpResponse('Can\'t view this page without submitting a form.')
