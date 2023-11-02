#===================================================================
# This file contains the views for the authentication app
#
#   Functions: 
#       login_user: This function logs in a user
#       logout_user: This function logs out a user
#===================================================================

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from user.models import User



# Login user function
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate user
        user = authenticate(request, 
                            username=username, 
                            password=password)
        # check if user is found using the model User to authenticate
        if user is not None:
            login(request, user)
            messages.success(request, 
                            "You have successfully logged in")
            return redirect("user_home")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")
    return render(request, "authenticate/login.html", {}) 


# Logout user function
def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect("login")