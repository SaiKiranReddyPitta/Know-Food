from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from kf_app.utils import *

# Create your views here.
def index(request):
	return render(request, "index.html")

def main(request):
	if request.method == 'GET':
		return render(request, "main.html")
	if request.method == 'POST':
		# print('###########',request.FILES)
		img_url = "http://localhost:8000/static/StdImages/"
		my_file = request.FILES['my_file']
		fs = FileSystemStorage('static/media')
		filename = fs.save(my_file.name, my_file)
		# classify(filename)
		veggie, conf = classify(filename)
		img_url += str(veggie) + ".jpg"
		data = {'veggie':veggie, 'conf':conf, 'img_url':img_url}
		return render(request, "veg.html", data)
	else:
		return HttpResponse("BAD REQUEST")

def register(request):
	if request.method == 'POST':
		return render(request, "register.html")
	if request.method == 'GET':
		return render(request, "register.html")
def forgot(request):
	return render(request, "forgot.html")