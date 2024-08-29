
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Shiva Admin Page"
admin.site.site_title = "Shiva Admin Portal"
admin.site.index_title = "Welcome to Shiva Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
    path('users/', include('users.urls')),
]

