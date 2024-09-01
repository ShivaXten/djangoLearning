
from django.contrib import admin
from django.urls import path, include
#this is to show the image 
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Shiva Admin Page"
admin.site.site_title = "Shiva Admin Portal"
admin.site.index_title = "Welcome to Shiva Portal"

urlpatterns = [
    path('',include('mywebsite.urls')),
    path('admin/', admin.site.urls),
    path('base/',include('base.urls')),
    path('users/', include('usersapp.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

