from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages,auth
# def demo1(request):
#     obj1=about.objects.all()
#     return render(request,"login.html",{'results':obj1})
def out(request):
    auth.logout(request)
    return redirect('/')

def log(request):
    if request.method=='POST':
        loginunmae=request.POST['username']
        loginpswd=request.POST['pswd']
        loginuser=auth.authenticate(username=loginunmae,password=loginpswd)

        if loginuser is not None:
            auth.login(request,loginuser)
            return redirect('/')
        else:
            messages.info(request,"Invalied Credentials")
            return redirect('loggin')

    return render(request, "login.html")


def register(request):
    if request.method=='POST':
        uname=request.POST['username']
        fname = request.POST['firstname']
        lnmae=request.POST['lastname']
        mail = request.POST['email']
        paswd = request.POST['password']
        cpaswd = request.POST['cpassword']
        if paswd==cpaswd:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username is already exists")
                return redirect('register')
            elif User.objects.filter(email=mail).exists():
                messages.info(request,"mail id is already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=uname, first_name=fname, last_name=lnmae, email=mail, password=paswd)
                user.save()
                return redirect('loggin')
                # messages.info("Registration is successfully")
                # return redirect('register')
        else:
            return redirect("register")
        return redirect('/')
    return render(request, "register.html")
# Create your views here.
