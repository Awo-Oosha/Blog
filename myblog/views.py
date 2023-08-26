from django.shortcuts import render
from .models import Post, Category
from django.core.paginator import Paginator
from django.conf import settings
import random

# Create your views here.

def homeView(request):
    post = Post.objects.filter(status = 'P').order_by('-pub_date')
    trends = Post.objects.filter(view_counts__gt=0).order_by('-view_counts')[:10]
    # pagination 
    paginator = Paginator(post, settings.PAGINATION_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    category =  Category.objects.all()

    query = request.GET.get('query')
    result = []
    if query:
        result = Post.objects.filter(title__icontains= query) | Post.objects.filter(content__icontains=query)

    context = {
        'posts': page_obj,
        'query': query,
        'results': result,
        'categories': category,
        'page_obj': page_obj,
        'trends': trends,
    }
    return render(request, 'myblog/home.html', context)

def searchView(request):
    query = request.GET.get('query')
    result = []
    if query:
        result = Post.objects.filter(title__icontains= query) | Post.objects.filter(content__icontains=query)

    return render(request, 'myblog/search.html', {'result': result})

def postDetail(request, slug):
    try:
        post = Post.objects.get(slug = slug)
        post.view_counts += 1
        post.save()
    except Post.DoesNotExist:
        post = None

    context = {
        'post': post
    }

    return render(request, 'myblog/post_detail.html', context)

def categoryDetail(request, name):
    try: 
        category = Category.objects.get(name = name)
    except Category.DoesNotExist:
        category = None

    

    context = {
        'category': category
    }
    return render(request, 'myblog/category_detail.html')

