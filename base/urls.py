from django.urls import path
from .import views
#for the image 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('room/',views.room, name="room"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
