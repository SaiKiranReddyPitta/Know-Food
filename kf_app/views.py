from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from kf_app.utils import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['pass']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			auth_login(request, user)
			return redirect('/main')
		else:
			response = {
			'message':'Wrong Credentials'
			}
			return render(request, 'index.html', response)
	return render(request, "index.html")

@login_required(login_url='/')
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
		nutrition_url = {
		'Banana':"https://www.nutritionvalue.org/Bananas%2C_raw_nutritional_value.html", 
		'Bell Pepper':"https://www.nutritionvalue.org/Peppers%2C_raw%2C_green%2C_sweet_nutritional_value.html", 
		'Cabbage':"https://www.nutritionvalue.org/Cabbage%2C_raw_nutritional_value.html", 
		'Carrot':"https://www.nutritionvalue.org/Carrots%2C_raw_nutritional_value.html", 
		'Cauliflower':"https://www.nutritionvalue.org/Cauliflower%2C_raw_nutritional_value.html", 
		'Cucumber':"https://www.nutritionvalue.org/Cucumber%2C_raw%2C_with_peel_nutritional_value.html", 
		'Green Bean':"https://www.nutritionvalue.org/Beans%2C_raw%2C_green%2C_snap_nutritional_value.html", 
		'Okra':"https://www.nutritionvalue.org/Okra%2C_raw_nutritional_value.html", 
		'Onion':"https://www.nutritionvalue.org/Onions%2C_raw_nutritional_value.html",
		'Pea':"https://www.nutritionvalue.org/Peas%2C_raw%2C_green_nutritional_value.html", 
		'Pepper':"https://www.nutritionvalue.org/Peppers%2C_raw%2C_green%2C_sweet_nutritional_value.html", 
		'Potato':"https://www.nutritionvalue.org/Potatoes%2C_skin%2C_raw_nutritional_value.html", 
		'Pumpkin':"https://www.nutritionvalue.org/Pumpkin%2C_raw_nutritional_value.html", 
		'Radish':"https://www.nutritionvalue.org/Radishes%2C_raw%2C_white_icicle_nutritional_value.html", 
		'Squash':"https://www.nutritionvalue.org/Pumpkin%2C_raw_nutritional_value.html", 
		'Sweet Potato':"https://www.nutritionvalue.org/Sweet_potato%2C_unprepared%2C_raw_nutritional_value.html", 
		'Tomato':"https://www.nutritionvalue.org/Tomatoes%2C_raw%2C_orange_nutritional_value.html", 
		'Yam':"https://www.nutritionvalue.org/Sweet_potato%2C_unprepared%2C_raw_nutritional_value.html"
		}
		img_url += str(veggie) + ".jpg"
		data = {'veggie':veggie, 'conf':conf, 'img_url':img_url, 'nutrition_url':nutrition_url[veggie]}
		return render(request, "veg.html", data)


def register(request):
	if request.method == 'POST':
		return render(request, "register.html")
	if request.method == 'GET':
		return render(request, "register.html")

def logout(request):
    auth_logout(request)
    return redirect('/')

def forgot(request):
	return render(request, "forgot.html")

def profile(request):
	return render(request, "profile.html")