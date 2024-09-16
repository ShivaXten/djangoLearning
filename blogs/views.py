
from rest_framework import viewsets
from .serializers import BlogReadOnlySerializer
from .models import Blog


class BlogReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogReadOnlySerializer
