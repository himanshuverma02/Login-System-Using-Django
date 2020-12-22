from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth 
from django.contrib import messages
def home(request):
    return render(request,"home.html", )

def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username ,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("userlogin")
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('loginpage')

    else:    
        return render(request ,'loginpage.html' )
    





def signup(request):

    if request.method == 'POST':
        first_name = request.POST['first_name'] 
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect ('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect ('signup')
            else:    
                user = User.objects.create_user(username= username, password=password1, email=email , first_name=first_name, last_name=last_name)
                user.save();
                print('user signedup')
                return redirect('loginpage')
        else:
            messages.info(request,'Password not matching')
            return redirect ('signup')
    else:    
        return render(request , "signup.html" ) 



def userlogin(request):
     return render(request , "userlogin.html")






def form(request):
    return render(request, 'form.html')