from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request, 'blog/index.html', context)

def blog(request):
    context={}
    return render(request, 'blog/blog.html', context)