from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.
def all_blog(request):
	obj=Blog.objects.order_by('-date')
	return render(request,'blog/all_blog.html',{'Blogs':obj})
def detail(request,blog_id):
	blog=get_object_or_404(Blog, pk=blog_id)
	return render(request,'blog/detail.html',{'blog':blog})