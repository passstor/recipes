from django.shortcuts import render,get_object_or_404
from .models import blog as Blog

def home(request):
    return render(request,'blog/home.html')

def all_blog(request):
    blogs=Blog.objects.all()
    return render(request,'blog/all_blog.html',{'blogs':blogs})

def detail_blog(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/detail_blog.html',{'blog':blog})