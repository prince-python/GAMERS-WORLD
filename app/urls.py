from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('contact/',views.contact),
    path('games/',views.games ,name='game'),
    path('gameview/<int:id>/',views.gameview),
    path('formsave/',views.formsave),
    path('login/',views.login),
    path('send/',views.send),
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
