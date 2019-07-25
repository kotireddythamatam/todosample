# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import blog_posts
# Create your views here.

class PostsForm(ModelForm):
    class Meta:
        model = blog_posts
        fields = ['id', 'title', 'description', 'status']

def post_list(request, template_name='blog_posts/post_list.html'):
    posts = blog_posts.objects.all()
    data = {}
    data['object_list'] = posts
    return render(request, template_name, data)

def post_create(request, template_name='blog_posts/post_form.html'):
    form = PostsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blog_posts:post_list')
    return render(request, template_name, {'form': form})

def post_update(request, pk, template_name='blog_posts/post_form.html'):
    post = get_object_or_404(blog_posts, pk=pk)
    form = PostsForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('blog_posts:post_list')
    return render(request, template_name, {'form': form})

def post_delete(request, pk, template_name='blog_posts/post_delete.html'):
    post = get_object_or_404(blog_posts, pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('blog_posts:post_list')
    return render(request, template_name, {'object': post})

# def post_search(request):
#     if request.method == 'GET': # this will be GET now
#         task_name =  request.GET.get('search') # do some research what it does
#         try:
#             results = blog_posts.objects.filter(bookname__icontains=task_name) # filter returns a list so you might consider skip except part
#         return render(request,"search.html",{"tasks":results})
#     else:
#         return render(request,"search.html",{})
