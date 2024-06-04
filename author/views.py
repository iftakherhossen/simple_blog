from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import get_user_model, authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import forms
from posts.models import Post

# Create your views here.
def author_profile(request, username):
    User = get_user_model()
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author.id)
    return render(request, 'author_profile.html', {'author': author, 'posts': posts})

def signup(request):
    if request.method == 'POST':
        signup_form = forms.SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, 'Account Created Successfully!')
            return redirect ('profile')
    else:
        signup_form = forms.SignUpForm(request.POST)
        
    return render(request, 'authentication.html', {'form': signup_form, 'heading': 'Create New Account', 'btn_text': 'Create'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.success(request, 'Logged in Successfully!')
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'Login Information is Incorrect!')
                return redirect('signup')
    else:
        form = AuthenticationForm()
        return render(request, 'authentication.html', {'form':form, 'heading': 'Login to Your Account', 'btn_text': 'Login'})

@login_required 
def profile(request):
    data = Post.objects.filter(author=request.user)
    return render(request, 'profile.html', {'data':data})

@login_required    
def update_profile(request):
    if request.method == 'POST':
        profile_form = forms.UpdateUserData(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully!')
            return redirect ('profile')
    else:
        profile_form = forms.UpdateUserData(instance=request.user)
        
    return render(request, 'update_profile.html', {'form': profile_form})

@login_required
def change_password(request):
    if request.method == 'POST':
        change_pass_form = PasswordChangeForm(request.user, data=request.POST)
        if change_pass_form.is_valid():
            change_pass_form.save()
            messages.success(request, 'Password Updated Successfully!')
            update_session_auth_hash(request, change_pass_form.user)
            return redirect ('profile')
    else:
        change_pass_form = PasswordChangeForm(user=request.user)
        
    return render(request, 'change_password.html', {'form': change_pass_form})

@login_required
def forgot_password(request):
    if request.method == 'POST':
        forgot_pass_form = SetPasswordForm(user=request.user, data=request.POST)
        if forgot_pass_form.is_valid():
            forgot_pass_form.save()
            update_session_auth_hash(request, forgot_pass_form.user)
            return redirect('profile')
    else:
        forgot_pass_form = SetPasswordForm(user=request.user)
    return render(request, 'forgot_password.html', {'form': forgot_pass_form})

@login_required 
def user_logout(request):
    logout(request)
    return redirect('login')