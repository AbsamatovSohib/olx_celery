from .models import Home
from .serializer import HomeSerializer
from .parser import celery_task
from rest_framework import generics


class HomeApiView(generics.ListAPIView):
    celery_task.delay()
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
