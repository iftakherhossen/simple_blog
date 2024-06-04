from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from . import models

# Create your views here.
def view_post(request, slug):
    user = request.user
    post = models.Post.objects.get(slug=slug)
    return render(request, 'view_post.html', {'post': post, 'user': user})

@login_required    
def create_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            # post_form.cleaned_data['author'] = request.user
            post_form.instance.author = request.user
            post_form.save()
            return redirect ('create_post')
    else:
        post_form = forms.PostForm(request.POST)
        
    return render(request, 'create_post.html', {'form': post_form})

@login_required 
def edit_post(request, id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect ('home')
        
    return render(request, 'edit_post.html', {'form': post_form})

@login_required 
def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('home')