from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import wikiEntry

# Create your views here.

def index(request):
	entry = get_object_or_404(wikiEntry, pk=1)
	return render(request, 'test.html', {entry.search : entry.search_date})
