from django.shortcuts import render, get_object_or_404
from blog.models import Blog


def all_blog(request):
    posts = Blog.objects.all()
    return render(request, 'blog/all_blog.html', {'posts': posts})


def blog_detail(request, post_id):
    detail = get_object_or_404(Blog, pk=post_id)
    return render(request, 'blog/blog_detail.html', {'detail': detail})
