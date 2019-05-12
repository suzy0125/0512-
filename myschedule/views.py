from django.shortcuts import render, get_object_or_404, redirect
from .models import Schedule
from .forms import PostForm
from django.utils import timezone
# Create your views here.

def home(request):
    posts = Schedule.objects
    return render(request, 'myschedule/home.html', {'posts':posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Schedule, pk = post_id)
    return render (request, 'myschedule/detail.html', {'post':post_detail})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect ('detail', post_id=post.pk)
    else:
        form = PostForm()
    return render(request, 'myschedule/new.html', {'form':form})

def post_edit(request, post_id):
    post = get_object_or_404(Schedule, pk = post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect ('detail', post_id=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'myschedule/edit.html', {'form':form})

def post_delete(request,post_id):
    post = get_object_or_404(Schedule, pk=post_id)
    post.delete()
    return redirect('home')