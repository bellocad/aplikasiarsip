from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('dokumen/', views.dokumen, name='dokumen'),
    path('pts/<str:pk>/', views.pts, name='pts'),
    path('dokumen_detail/<path:pk>/', views.dokumenDetail, name='dokumenDetail'),
    path('upload_dokumen/', views.uploadDokumen, name="upload_dokumen"),

    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('order_order/<str:pk>/', views.orderOrder, name="order_order"),

    path('daftar_pts', views.daftarPTS, name="daftarPTS"),
    path('rekomendasi', views.rekom, name="rekomendasi"),
    path('deleteRekom/<str:pk>/', views.deleteRekom, name='deleteRekom'),

    path('search', views.search, name='search'),

    path('surat_keputusan', views.SKeputusan, name='surat_keputusan'),
    path('deleteSK/<str:pk>/', views.deleteSK, name='deleteSK'),


]
