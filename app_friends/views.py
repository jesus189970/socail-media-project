from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *
# Create your views here.
def index(request):
    return redirect('/main')

def main_page(request):
    return render(request, 'main.html')

def register(request):
    if request.method=='POST':
        errors=User.objects.validator(request.POST)
        if errors:
            for error in errors:
                messages.error(request, errors[error])
            return redirect('/')
        user_pw=request.POST['pw']
        hash_pw=bcrypt.hashpw(user_pw.encode(), bcrypt.gensalt()).decode()
        print(hash_pw)
        new_user=User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=hash_pw, birth=request.POST['birth'])
        print(new_user)
        request.session['user_id']=new_user.id
        request.session['user_name']=f"{new_user.name} {new_user.alias}"
        return redirect('/friends')
    return redirect('/')

def friends(request):
    user = User.objects.get(id=request.session['user_id'])
    friends = user.friends.all()
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'self': User.objects.get(id=request.session['user_id']),
        'user': user.friends.all(),
        'users': User.objects.all()
    }
    return render(request, 'friends.html', context)

def login(request):
    if request.method=='POST':
        logged_user=User.objects.filter(email=request.POST['email'])
        if logged_user:
            logged_user=logged_user[0] 
        if bcrypt.checkpw(request.POST['pw'].encode(), logged_user.password.encode()):
            request.session['user_id']=logged_user.id
            request.session['user_name']=logged_user.alias
            return redirect('/friends')
    return redirect('/')

def logout(request):
    del request.session['user_id']
    del request.session['user_name']
    return redirect('/')

def profile(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'profile.html', context)

def add_friend(request, user_id):
    user = User.objects.get(id=request.session['user_id'])
    user2 = user_id
    user.friends.add(user2)
    user.save()
    return redirect('/friends')

def remove_friend(request, user_id):
    user = User.objects.get(id=request.session['user_id'])
    user2 = user_id
    user.friends.remove(user2)
    user.save()
    return redirect('/friends')