from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

      path('', views.home, name='home'),
      path('login', views.login, name='login'),
      path('signup', views.signup, name='signup'),
      path('Add-to-note', views.add_tonote , name='add_tonote'),
      path('delete_notes/<int:id>' , views.delete_notes , name='delete_notes')

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
