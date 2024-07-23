from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CustomerForm
# Create your views here.


def account(request):
    return render(request, 'account/index.html')


def login(request):
    return render(request, 'account/login.html')


def signup(request):
    password1 = request.POST.get('password')
    password2 = request.POST.get('password2')
    if request.method == 'POST':
        if password1 == password2:
            form = CustomerForm(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.save()
                return redirect('login')
    else:
        form = CustomerForm()
    return render(request, 'account/signup.html')
