from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib import messages
from .models import Account
# from django.views.decorators.csrf import csrf_exempt

# open the login page in start
def startPoint(request):
  return render(request, "authentication/login.html")

# @csrf_exempt
def login(request):
  if request.method == "POST":
    userEmail = request.POST.get('email')
    password = request.POST.get('password')
    
    user = authenticate(email=userEmail, password=password)
    if user is not None:
      messages.success(request, "Welcome!")
      # return JsonResponse({"results": True})
      return render(request, "authentication/index.html")
    else:
      messages.error(request, "Failed to login")
      return JsonResponse({"results": False})
  
  return render(request, "authentication/login.html")


def signup(request):
  
  if request.method == "POST":
    userName = request.POST.get('user_name')
    userEmail = request.POST.get('email')
    password = request.POST.get('password')

    user = Accounts.objects.create_user(userEmail, userName, password)
    user.save()

    return render(request, "authentication/login.html")
  
  return render(request, "authentication/signin.html")  
