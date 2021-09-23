from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import AddComment, AddPost, Services
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
error_message = ''
login_error = ''
comment_error = ''
contact_error = ''
counter = 0


def index(request):
    global contact_error
    posts = AddPost.objects.all()
    services = Services.objects.all()
    if request.method == "POST":
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        if email == '' or subject == '' or message == '':
            contact_error = 'Please fill all text below!'
            return redirect('/')
        else:
            contact_error = ''
            email_receiver = [settings.EMAIL_HOST_USER, ]
            email_from = email
            send_mail(subject, message, email_from, email_receiver)
        email = ''
        subject = ''
        message = ''
    else:
        return render(request, 'index.html', {
            'posts': posts,
            'contact_error': contact_error,
            'services': services
        })
    return render(request, 'index.html', {
        'posts': posts,
        'contact_error': contact_error,
        'services' : services
    })


def register(request):
    global error_message
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['comfirm_password']

        if password == re_password:
            if User.objects.filter(username=username).exists():
                error_message = "This username is already exists!"
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                error_message = "This email is already exists!"
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                error_message = ''
        else:
            error_message = "Not same password!"
            return redirect('register')

    else:
        return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html', {'error_message': error_message})


def login(request):
    global login_error
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(
            username=username, email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            login_error = "Credentials Invalid"
            return redirect('login')

    return render(request, 'login.html', {'login_error': login_error})


def logout(request):
    auth.logout(request)
    return redirect('/')


def post(request, pk):
    global comment_error
    comments = AddComment.objects.all()
    posts = AddPost.objects.all()
    post = AddPost.objects.get(id=pk)
    username = request.user.username
    if request.method == 'POST':
        text = request.POST['comment_text']
        if text == '':
            comment_error = 'Please enter text!'
            text = ''
            return redirect('/post/' + str(post.pk))
        else:
            comment_error = ''
            comment = AddComment.objects.create(
                post=post, name=username, body=text)
            comment.save()
            text = ''
    else:
        return render(request, 'post.html', {
            'post': post,
            'comments': comments,
            'posts': posts,
            'comment_error': comment_error,
        })
    return render(request, 'post.html', {
        'post': post,
        'comments': comments,
        'posts': posts,
        'comment_error': comment_error,
    })


def service(request, pk):
    service = Services.objects.get(id=pk)
    return render(request, 'services.html',{
        'service': service
    })
