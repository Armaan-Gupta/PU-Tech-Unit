from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required      #this decorator is provided by django and it tells you to login if you are not already


# Create your views here.
def register(request):
    if request.method == 'POST':     #Used to validate form data if the form method is post
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()           #saves the user
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required             # After logging in this will redirect to the profile page only, and not to the home page
def profile(request):       # This feature is very helpful in all web apps. This is specified by the next parameter in the url
    return render(request, 'users/profile.html')

#types of flash messages:
#message.debug
#message.info
#message.success
#message.warning
#message.error

