from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from main.models import film, language

# Create your views here.
def index(request):
	if request.method == 'GET':
		return HttpResponse("API Sample")

@csrf_exempt
def films(request):
	if request.method == 'GET':
		films = serializers.serialize('json', film.objects.all())
		return HttpResponse(films)
	elif request.method == 'POST':
		print request.body

@csrf_exempt
def languages(request):
	if request.method == 'GET':
		languages = serializers.serialize('json', language.objects.all())
		return HttpResponse(languages)
	elif request.method == 'POST':
		print request.body

@csrf_exempt
def languages_language(request, id):
	if request.method == 'GET':
		language_single = serializers.serialize('json', language.objects.filter(pk=id))
		return HttpResponse(language_single)
	elif request.method == 'POST':
		print request.body