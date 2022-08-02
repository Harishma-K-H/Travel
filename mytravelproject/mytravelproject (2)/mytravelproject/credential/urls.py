from django.urls import path
from . import views
urlpatterns=[
    path('register',views.register,name="register"),
    path("login",views.log,name="loggin"),
    path("logout",views.out,name="loggout"),
    # path("demo1",views.demo1,name="demo1"),


]