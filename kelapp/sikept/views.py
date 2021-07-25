from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
# create views
from .models import *
from .forms import OrderForm, DokumenForm
from .decorators import unauthenticated_user
from .filters import DokumenFilter, OrderFilter


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
    return render(request, 'sikept/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def home(request):
    orders = Order.objects.all().order_by('-date_created')
    pts = Pts.objects.all()
    dokumen = Dokumen.objects.all()

    total_pts = pts.count()
    total_orders = orders.count()
    total_dokumen = dokumen.count()

    rekomendasi = dokumen.filter(category='Rekomendasi').count()
    sk = dokumen.filter(category__startswith='SK').count()
    dikirim = orders.filter(status='Dikirim').count()
    pending = orders.filter(status='Pending').count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    page = request.GET.get('page', 1)
    paginator = Paginator(orders, 10)
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    context = {'order': orders, 'pts': pts, 'total_pts': total_pts,
               'total_orders': total_orders, 'total_dokumen': total_dokumen,
               'sk': sk, 'dikirim': dikirim, 'pending': pending, 'rekomendasi': rekomendasi,
               'myFilter': myFilter}

    return render(request, 'sikept/dashboard.html', context)


def daftarPTS(request):
    pts = Pts.objects.all()
    return render(request, 'sikept/daftar_pts.html', {'pts': pts})


@login_required(login_url='login')
def dokumen(request):
    dokumen = Dokumen.objects.all().order_by('-date_created')

    total_dokumen = dokumen.count()
    total_rekomendasi = dokumen.filter(
        category__startswith='Rekomendasi').count()
    total_sk = dokumen.filter(category__startswith='SK').count()
    total_srtpermohonan = dokumen.filter(category='Surat Permohonan').count()

    myFilter = DokumenFilter(request.GET, queryset=dokumen)
    dokumen = myFilter.qs

    page = request.GET.get('page', 1)
    paginator = Paginator(dokumen, 10)
    try:
        dokumen = paginator.page(page)
    except PageNotAnInteger:
        dokumen = paginator.page(1)
    except EmptyPage:
        dokumen = paginator.page(paginator.num_pages)

    return render(request, 'sikept/dokumen.html', {
        'dok': dokumen,
        'total_dokumen': total_dokumen,
        'total_rekomendasi': total_rekomendasi,
        'total_sk': total_sk,
        'total_srt': total_srtpermohonan,
        'myFilter': myFilter})


def dokumenDetail(request, pk):
    dokumenDetail = Dokumen.objects.get(nomor=pk)

    context = {'dokumenDetail': dokumenDetail}
    return render(request, 'sikept/dokumen_detail.html', context)


def uploadDokumen(request):
    form = DokumenForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = DokumenForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Berhasil Menambah Dokumen'))
            return redirect('dokumen')

    context = {'form': form}
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

    context = {
        'jenis_akta': jenis_akta,
        'jenis_sk': jenis_sk,
        'pts': pts, 'orders': orders,
        'order_count': order_count,
        'jenis_rekom': jenis_rekom,
        'jenis_pengesahan': jenis_pengesahan
    }
    return render(request, 'sikept/pts.html', context)


def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'sikept/order_form.html', context)


def orderOrder(request, pk):
    dokumen = Dokumen.objects.get(id=pk)
    form = OrderForm(initial={'nomor': dokumen})
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dokumen')

    context = {'form': form}
    return render(request, 'sikept/order_form.html', context)


def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, ('Informasi Berhasil diupdate.'))
            return redirect('../../')

    context = {'form': form}
    return render(request, 'sikept/order_form.html', context)


# def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    # if request.method == "POST":
    # order.delete()
    # return redirect('/')

    #context = {'item': order}
    # return render(request, 'sikept/delete.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect('../../')


def deleteRekom(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect('rekomendasi')


def deleteSK(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect('surat_keputusan')


def rekom(request):
    orders = Order.objects.all().order_by('-date_created')
    dokumen = Dokumen.objects.all()
    rekomendasi = dokumen.filter(category__startswith='Rekomendasi')
    rekomorder = orders.filter(Jenis__startswith='Rekomendasi')

    total_orders = orders.count()
    total_dokumen = dokumen.count()
    total_rekomendasi = rekomendasi.count()

    dikirim = orders.filter(status='Dikirim').count()
    pending = orders.filter(status='Pending').count()

    myFilter = DokumenFilter(request.GET, queryset=rekomendasi)
    rekomendasi = myFilter.qs

    myFilter2 = OrderFilter(request.GET, queryset=rekomorder)
    rekomorder = myFilter2.qs

    page = request.GET.get('page', 1)
    paginator = Paginator(orders, 10)
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    context = {'order': orders,
               'total_orders': total_orders,
               'total_dokumen': total_dokumen,
               'dikirim': dikirim,
               'pending': pending,
               'rekomendasi': rekomendasi,
               'total_rekomendasi': total_rekomendasi,
               'myFilter': myFilter,
               'myFilter2': myFilter2,
               'rekomorder': rekomorder
               }

    return render(request, 'sikept/rekomendasi.html', context)


def SKeputusan(request):
    orders = Order.objects.all().order_by('-date_created')
    pts = Pts.objects.all()
    dokumen = Dokumen.objects.all()
    sk = orders.filter(Jenis__startswith='SK')

    total_sk = pts.count()
    total_orders = orders.count()
    total_dokumen = dokumen.count()

    rekomendasi = dokumen.filter(category='Rekomendasi').count()
    dikirim = orders.filter(status='Dikirim').count()
    pending = orders.filter(status='Pending').count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    page = request.GET.get('page', 1)
    paginator = Paginator(orders, 10)
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    context = {'order': orders, 'pts': pts, 'total_sk': total_sk,
               'total_orders': total_orders, 'total_dokumen': total_dokumen,
               'sk': sk, 'dikirim': dikirim, 'pending': pending, 'rekomendasi': rekomendasi,
               'myFilter': myFilter}

    return render(request, 'sikept/surat_keputusan.html', context)


def search(request):
    members = Dokumen.objects.filter(Q(nomor=request.GET.get(
        'search')) | Q(perihal=request.GET.get('search')))
    return render(request, 'dokumen.html', {'members': members})
