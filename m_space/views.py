from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Post, Comment
from .forms import CommentForm, PostForm, CommentCommentForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def login(request):
    if request.user.is_authenticated():
        return redirect('/post_list/')
    else:
        return render(request, 'm_space/login.html')



def logout(request):
    auth_logout(request)
    return redirect('/')

def post_list(request):

    template_name = 'm_space/post_list.html'
    posts = Post.objects.all()
    if request.method == "POST":
        form_post = PostForm(request.POST)
        if form_post.is_valid():
            post = form_post.save(commit=False)
            post.author = request.user
            post.created = timezone.now()
            post.save()
            return redirect('/')
    else:
        form_post = PostForm()


    return render(request, template_name, {'posts': posts, 'form_post': form_post})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form_comment = CommentForm(request.POST)
        if form_comment.is_valid():
            comment = form_comment.save(commit=False)
            comment.post = post
            comment.name = request.user
            comment.save()
            return redirect('/')
    else:
        form_comment = CommentForm()
    return render(request, 'm_space/add_comment_to_post.html', {'form_comment': form_comment})

def add_comment_to_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form_commentcomment = CommentCommentForm(request.POST)
        if form_commentcomment.is_valid():
            commentcomment = form_commentcomment.save(commit=False)
            commentcomment.comment = comment
            commentcomment.name = request.user
            commentcomment.save()
            return redirect('/')
    else:
        form_commentcomment = CommentCommentForm()
    return render(request, 'm_space/add_comment_to_comment.html', {'form_commentcomment': form_commentcomment})
