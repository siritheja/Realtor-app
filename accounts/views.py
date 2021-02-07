from django.shortcuts import render , redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact
# Create your views here.


def register(request):
    if request.method == "POST":
        #messages.error(request,'Testing error message')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already exists')
                return redirect('register')
            else:
                if len(password)<8 :
                    messages.error(request,'Password is too weak')
                    return redirect('register')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request,'Email already exists')
                        return redirect('register')
                    else:
                        # create user
                        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name= last_name)
                        #login after register
                        #auth.login(request, user)
                        user.save()
                        messages.success(request, 'You are now logged in.')
                        return redirect('login')
        else:
            messages.error(request,'Passwords do not match')
            return redirect('register')
    else :
        return render(request,'accounts/register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        print('user- ',user)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else :
            messages.error(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request,"You are now logged out")
        return redirect('login')

def dashboard(request):
    contact_list = Contact.objects.filter(user_id=request.user.id)
    context = {
        'user_contact' : contact_list, 
    }    
    return render(request,'accounts/dashboard.html',context)