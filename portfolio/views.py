from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
from .models import Post

def index(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        message = request.POST['message']

        send_mail(
            name , 
            phone_number,
            message ,
            settings.EMAIL_HOST_USER,
            [email],
        )
    context = {
        'posts': posts
    }
    return render(request , 'index.html' , context)