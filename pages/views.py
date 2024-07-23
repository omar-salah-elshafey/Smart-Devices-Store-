from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Logo, Cover, Blog, BlogCover, About, Contact, Message
from .forms import CommentForm, MessageForm
# Create your views here.


def pages(request):
    logoes = Logo.objects.all()
    covers = Cover.objects.all()
    return render(request, 'pages/index.html', {'logoes': logoes, 'covers': covers})


def blog(request):
    blogs = Blog.objects.all()
    blogscovers = BlogCover.objects.all()
    return render(request, 'pages/blog.html', {'blogs': blogs, 'blogscovers': blogscovers})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect('blog_detail', blog_id=blog_id)
    else:
        form = CommentForm()
    return render(request, 'pages/blog_detail.html', {'blog': blog, 'form': form})


def about(request):
    about = About.objects.all()
    return render(request, 'pages/about.html', {'about': about})


def contact(request):
    contact = Contact.objects.all()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect('contact')
    else:
        form = MessageForm()
    return render(request, 'pages/contact.html', {'contact': contact, 'form': form})

# def contact(request):
#     contact = Contact.objects.all()
#     name = request.POST.get('name')
#     email = request.POST.get('email')
#     body = request.POST.get('body')
#     data = Message(name=name, email=email, body=body)
#     data.save()
#     return render(request, 'pages/contact.html', {'contact': contact})
