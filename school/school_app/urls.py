from django.urls import path

from school_app import views

urlpatterns = [

    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/', views.register, name='register'),
    path('student/',views.student,name='student'),
    path('logout/',views.logout,name='logout'),

]