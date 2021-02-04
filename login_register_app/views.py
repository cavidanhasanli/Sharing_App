from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home_page')

        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')


# Userlerin logoutlari bu viewda aparilir
def logout(request):
    auth.logout(request)
    return redirect('login')


# Userlerin qeydiyyati bu viewda aparilir
def register(request):
    if request.method == 'POST':
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        user_name = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name,
                                                       password=password1,
                                                       email=email,)
                                                       # first_name=first_name,
                                                       # last_name=last_name)
                user.save()
                print('user created')

        else:
            messages.info(request, "password not matching...")
            return redirect('register')
        return redirect('login')

    else:
        return render(request, 'register.html')