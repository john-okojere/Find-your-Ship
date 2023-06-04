from django.shortcuts import render, redirect
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from .serializers import UserSerializer,  RegisterSerializer
from django.contrib.auth import login, authenticate
from .models import User
from .forms import RegisterForm
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from django.http import JsonResponse
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()

class UserDetailAPI(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


def homepage(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def media(request):
    return render(request, 'home/media.html')


def search_memberlist(request, name):
    if name.__len__() > 0:
        members = User.objects.filter(Q(username__icontains=name))
    else:
        members = User.objects.all()
    data = []
   
    for person in members:
        try: 
            if person.pastor:
                p = 't'
        except:
            p = 'f'
        data.append({
            'id':person.id,
            'username':person.username,
            'first_name':person.first_name,
            'last_name':person.last_name,
            'phone':person.phone,
            'email':person.email,
            'gender':person.gender,
            'role':person.role,
            'date_joined':person.date_joined,
            'pastor':p
        })
    return JsonResponse(data,safe=False, status=200)
    

def members(request):
    members = User.objects.all()
    return render(request, 'account/members.html',{'members':members})

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            rform = form.save(commit=False)
            rform.role = "USER"
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, f"New account created: {username}")
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'account/create.html', {'form': form})

@login_required
def profile(request):
        return render(request, 'account/profile.html')



class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'account/password/reset.html'
    email_template_name = 'account/password/reset_email.html'
    subject_template_name = 'account/password/reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('login')