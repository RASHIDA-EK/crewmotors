from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('views/', views.views, name='views'),


    path('list/views2/', views.views2, name='views2'),



    path('list/', views.list, name='list'),


    path('parts/', views.part, name='parts'),
    path('parts/p_view/add/', views.part_details, name='add'),

    path('parts/p_view/', views.parts_view, name='parts_view'),

    #services
    path('service/', views.service, name='service'),
    path('service/s_details/', views.s_details, name='ser_deails'),

    #search
    path('search/', views.search, name='search'),
    path('search2/', views.search2, name='search2'),
    

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
