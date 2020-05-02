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
		wikiEntry(search=request.POST, search_date=timezone.now()).save()
		return HttpResponse('SUPER YO')
	elif request.method == 'GET':
		return HttpResponse('YO WTF')