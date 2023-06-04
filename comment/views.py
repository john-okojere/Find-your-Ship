from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def wishes(request):
    wishes = Comment.objects.all().order_by('-date_added')
    return render(request, 'home/wishes.html', {'wishes':wishes})

def form(request):
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('wishes')
    else:
        form = CommentForm()
    return render(request, 'home/form.html',{'form':form})