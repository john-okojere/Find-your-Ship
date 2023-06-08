from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def wishes(request):
    wishes = Comment.objects.all().order_by('-date_added')
    return render(request, 'home/wishes.html', {'wishes':wishes})

@login_required
def form(request):
    wishes = Comment.objects.filter(user=request.user)
    if wishes:       
        return render(request, 'home/hbd_profile.html', {'wishes':wishes})
    else:
        if request.method == "POST":
            form = CommentForm(request.POST, request.FILES)
            if form.is_valid():
                f = form.save(commit=False)
                f.user = request.user
                form.save()
                return redirect('/')
        else:
            form = CommentForm()
        return render(request, 'home/form.html',{'form':form})
