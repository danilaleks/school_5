from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

@login_required
def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user == post.author:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('post_list')
        else:
            form = PostForm(instance=post)
        return render(request, 'edit_post.html', {'form': form})
    else:
        return redirect('post_list')
 def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})        
