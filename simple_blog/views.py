from django.shortcuts import render
from django.db.models import Count
from posts.models import Post
from categories.models import Category

# Create your views here.
def home(request, category_slug = None):  
    categories = Category.objects.annotate(post_count=Count('post')).filter(post_count__gt=0).order_by('-post_count')
    if category_slug is not None:
        category = Category.objects.get(slug=category_slug)
        posts = Post.objects.filter(category=category)
    else:
        posts = Post.objects.all().order_by('-id')
    return render(request, 'home.html', {'posts': posts, 'categories': categories})