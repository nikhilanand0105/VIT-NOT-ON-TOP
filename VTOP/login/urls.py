from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path("login/",views.student,name="student"),
    path("error/",views.error,name="error")

]
