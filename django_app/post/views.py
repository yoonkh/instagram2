from django.shortcuts import render, redirect

from .models import Post


def post_list(request):
    p1 = Post.objects.first()
    post = Post.objects.all()
    context = {
        'posts': post,
    }
    return render(request, 'post/post_list.html', context)


def post_delete(request, post_pk):
    if request.method == 'POST':
        print(request)
        print(request.POST)
    return redirect('post_list')
