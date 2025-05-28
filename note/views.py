from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def main(request):
    return render(request, 'index.html')

@login_required
def user_notes(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'index.html', {'notes': notes})

def detail(request, id):
    note = get_object_or_404(Note, id=id)
    return render(request, 'detail.html', {'note': note})

def create(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get('title')
        content = request.POST.get('content')
        note = Note.objects.create(user=user, title=title, content=content)
        return redirect('user-note')
    return render(request, 'detail.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("user-note")
    return render(request, 'signin.html')

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            user = User.objects.create(username=username, email=email)
            user.set_password(password1)
            user.save()
            return redirect('login')
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return redirect("login")

def edit(request, id):
    note = get_object_or_404(Note, id=id)
    if request.method == "POST":
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('user-note')
    return render(request, 'detail.html', {'note': note})

def delete(request, id):
    note = get_object_or_404(Note, id=id)
    note.delete()
    return redirect('user-note')

