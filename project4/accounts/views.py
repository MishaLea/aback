from django.http import JsonResponse
from django.http import Httpresponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from . import views

def login(request):
  if request.method == "POST":
    userName = request.POST.get['user_name']
    password = request.POST.get['password']
  
    user = authenticate(username=userName, password=password)
  
    if user is not None:
      login(request, user)
    return JsonResponse({"result": True})
  else:
    return JsonResponse({"result": False})



def signup(request):

  if request.method == "POST":
    userName = request.POST.get('user_name')
    userEmail = request.POST.get('email')
    password = request.POST.get('password')

    user = User.objects.create_user(userName, userEmail, password)
    user.name = user_name
    user.email = email
    user.password = password
    
    user.save()

    messages.success(request, "Your account has been created successfully.")

    return redirect("signup")

  return JsonResponse({"result": True})