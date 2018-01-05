from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from brainstorm.forms import  SignUpForm, PersonForm, LevelIncreaseForm
from django.contrib.auth import authenticate
from .models import Person,level
from django.contrib.auth import login as auth_login

# Create your views here.
#@login_required
def home(request):
	return render(request, 'index.html')

	
def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        
        
    else: 
    	return HttpResponse("invalid login")

 
def logout_view(request):
    logout(request)    	


def signup(request):
    if request.method == 'POST':
        form  = SignUpForm(request.POST)
        form2 = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if form2.is_valid():
            	new_user_form=form2.save(commit=False)
            	new_user_form.user=user
            	new_user_form.save()
            	auth_login(request, user)
            	return redirect('/brainstorm/login')

           
    else:
        form = SignUpForm()
        form2= PersonForm()
    return render(request, 'signup.html', {'form': form, 'form2':form2})



@login_required
def levels(request,levelnum): 
    current_user=Person.objects.get(user=request.user)
    current_user_level = current_user.current_level.levelnumber
    imageurl="static/brainstorm/images/"+level.objects.get(levelnumber=levelnum).pic+".jpg"
    if current_user_level != levelnum:
        return redirect('/brainstorm/levels/level'+str(current_user_level)+"/")
    else:
        if request.method=='POST':
            form=LevelIncreaseForm(request.POST)
            if form.is_valid():
                answer=form.cleaned_data['ans']
                correctans = level.objects.get(levelnumber=current_user_level).ans
                if answer==correctans:
                    current_user.increaselevel()
                    return redirect('/brainstorm/levels/level'+str(current_user_level)+"/")
                else:
                    return HttpResponse("wrong ans")
        else:
            form=LevelIncreaseForm()  
        return render(request,'level.html',{'form':form,'levelnum':levelnum,'imageurl':imageurl})
    return render(request,'level.html',{'username':username,'levelnumber':levelnumber,'imageurl':imageurl})


def results(request):
    all_users=Person.objects.all().order_by('current_level','levelentry')
    return render(request,'result.html')    






