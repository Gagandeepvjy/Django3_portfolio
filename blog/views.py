from django.shortcuts import render,get_object_or_404
from .models import blog
# Create your views here.
def all_blogs(request):
    blogs=blog.objects.all()
    return render(request,'blog/all_blogs.html',{'blogs':blogs})
def detail(request,blog_id):
    Blog=get_object_or_404(blog,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':Blog })
