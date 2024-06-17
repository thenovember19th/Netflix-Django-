from django.contrib import admin
from django.urls import path
from flix import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('signup/',views.signUp,name='signup'),
    path('home/',views.home,name='home'),
    path('login/',views.handleLogin,name='login'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('change_password/',views.change_password,name='change_password'),
]
