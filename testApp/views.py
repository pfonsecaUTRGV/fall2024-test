from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.

def home(request):

	records = Record.objects.all()


	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user  = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request,"Login Successfull")
			return redirect('home')
		else:
			messages.success(request,"Log in error")
			return redirect('home')
	else:
		return render(request, 'home.html', {'records':records})

#def login_user(request):
	#pass

def logout_user(request):
	logout(request)
	messages.success(request,"You have Logged Out")
	return redirect('home')

def register_user(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			#cleanned data separate an specific element and past it 
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request,"Sign In Successfull")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})
	return render(request, 'register.html', {'form':form})


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request,"Record Added")
				return redirect('home')

		return render(request, 'add_record.html', {'forms':form})
	else:
		return redirect('home')