from django.shortcuts import render
from django.http import JsonResponse
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'myapp/index.html', {'posts': posts})

def health_check(request):
    return JsonResponse({'status': 'ok', 'message': 'Server ishlayapti!'})
