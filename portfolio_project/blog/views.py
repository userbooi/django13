from django.shortcuts import render, get_object_or_404
from .models import Topic

# Create your views here.
def blog(request):
    info = Topic.objects.all()
    return render(request, 'blogs/blog.html', {'infos':info})

def detail(request, blog_id):
    blog = Topic.objects.get(id=blog_id)
    return render(request, 'blogs/detail.html', {'blog':blog})
