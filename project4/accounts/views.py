from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Account
from django.views.decorators.csrf import csrf_exempt
from rooms.views import Home

# open the login page in start
def startPoint(request):
  return render(request, "authentication/login.html")

@csrf_exempt
def login(request):
  if request.method == "POST":
    userEmail = request.POST.get('email')
    password = request.POST.get('password')
    
    user = authenticate(email=userEmail, password=password)
    if user is not None:
      messages.success(request, "Welcome!")
      return render(request, "authentication/index.html", {"login": True})
      # return redirect(Home)
    else:
      messages.error(request, "Failed to login")
      return JsonResponse({"results": False})
  else:
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
