from django.contrib import admin
from django.urls import path
from flix import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('signup/',views.signUp,name='signup'),
    path('home/',views.home,name='home'),
    path('login/',views.handleLogin,name='login'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('change_password/<str:token>/',views.change_password,name='change_password'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



