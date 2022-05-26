from django.shortcuts import render
from .models import blog as blog_model
def home(request):
    blogs=blog_model.objects.order_by('-date')[:3]
    return render(request,'blog/home.html',{'blogs':blogs})