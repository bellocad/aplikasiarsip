from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
#create views
from .models import *
from .forms import OrderForm, DokumenForm
from .decorators import unauthenticated_user

# Create your views here.
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render (request, 'sikept/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def home(request):
    orders = Order.objects.all().order_by('-date_created')
    pts = Pts.objects.all()

    total_pts = pts.count()

    total_orders = orders.count()
    dikirim = orders.filter(status='Dikirim').count()
    pending = orders.filter(status='Pending').count()

    page = request.GET.get('page', 1)
    paginator = Paginator(orders, 10)
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    context = {'order':orders, 'pts':pts, 'total_pts':total_pts, 
    'total_orders':total_orders ,'dikirim':dikirim, 'pending':pending}

    return render(request, 'sikept/dashboard.html', context)

def daftarPTS(request):
    pts = Pts.objects.all()
    return render(request, 'sikept/daftar_pts.html', {'pts':pts})

@login_required(login_url='login')
def dokumen(request):
    dokumen = Dokumen.objects.all().order_by('-date_created')
    
    page = request.GET.get('page', 1)
    paginator = Paginator(dokumen, 10)
    try:
        dokumen = paginator.page(page)
    except PageNotAnInteger:
        dokumen = paginator.page(1)
    except EmptyPage:
        dokumen = paginator.page(paginator.num_pages)

    return render(request, 'sikept/dokumen.html',{'dok':dokumen})

def dokumenDetail (request, pk):
    dokumenDetail = Dokumen.objects.get(nomor=pk)

    context = {'dokumenDetail':dokumenDetail}
    return render(request, 'sikept/dokumen_detail.html', context)

def uploadDokumen(request):
    form = DokumenForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = DokumenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dokumen')

    context = {'form':form}
    return render(request, 'sikept/order_form.html', context)

def pts(request, pk):
    pts = Pts.objects.get(nama_pts=pk)
    
    orders = pts.order_set.all()
    order_count = orders.count()

    jenis_sk = orders.filter(Jenis='SK')
    jenis_akta = orders.filter(Jenis='Akta')
    jenis_pengesahan = orders.filter(Jenis='SK Menkumham')
    jenis_rekom = orders.filter(Jenis='Rekomendasi')
    jenis_surat = orders.filter(Jenis='Surat')

    context = {'jenis_akta':jenis_akta, 'jenis_sk':jenis_sk, 'pts':pts, 'orders':orders, 
                'order_count':order_count, }
    return render(request, 'sikept/pts.html', context)

def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'sikept/order_form.html', context)
    
def orderOrder(request, pk):
    dokumen = Dokumen.objects.get(id=pk)
    form = OrderForm(initial={'nomor':dokumen})
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'sikept/order_form.html', context)

def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'sikept/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request, 'sikept/delete.html', context)