from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from products.forms import PhoneForm, TabForm, WatchForm, AirpodForm
from .models import Phone, Tab, Watch, Airpod, AirpodsCover,  PhonesCover, TabsCover, WatchesCover

# Create your views here.


def phones(request):
    phones = Phone.objects.all()
    phonescovers = PhonesCover.objects.all()
    return render(request, 'products/phones.html', {'phones': phones, 'phonescovers': phonescovers})


def tablets(request):
    tabs = Tab.objects.all()
    tabscovers = TabsCover.objects.all()
    return render(request, 'products/tablets.html', {'tabs': tabs, 'tabscovers': tabscovers})


def watches(request):
    watches = Watch.objects.all()
    watchescovers = WatchesCover.objects.all()
    return render(request, 'products/watches.html', {'watches': watches, 'watchescovers': watchescovers})


def airpods(request):
    airpods = Airpod.objects.all()
    airpodscovers = AirpodsCover.objects.all()
    return render(request, 'products/airpods.html', {'airpods': airpods, 'airpodscovers': airpodscovers})


def phone_detail(request, phone_name):
    phone = get_object_or_404(Phone, name=phone_name)
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.phone = phone
            comment.save()
            return redirect('phone_detail', phone_name=phone_name)
    else:
        form = PhoneForm()
    return render(request, 'products/phone_detail.html', {'phone': phone, 'form': form})


def tab_detail(request, tab_name):
    tab = get_object_or_404(Tab, name=tab_name)
    if request.method == 'POST':
        form = TabForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.tab = tab
            comment.save()
            return redirect('tab_detail', tab_name=tab_name)
    else:
        form = PhoneForm()
    return render(request, 'products/tab_detail.html', {'tab': tab, 'form': form})


def watch_detail(request, watch_name):
    watch = get_object_or_404(Watch, name=watch_name)
    if request.method == 'POST':
        form = WatchForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.watch = watch
            comment.save()
            return redirect('watch_detail', watch_name=watch_name)
    else:
        form = PhoneForm()
    return render(request, 'products/watch_detail.html', {'watch': watch, 'form': form})


def airpod_detail(request, airpod_name):
    airpod = get_object_or_404(Airpod, name=airpod_name)
    if request.method == 'POST':
        form = AirpodForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.airpod = airpod
            comment.save()
            return redirect('airpod_detail', airpod_name=airpod_name)
    else:
        form = PhoneForm()
    return render(request, 'products/airpod_detail.html', {'airpod': airpod, 'form': form})
