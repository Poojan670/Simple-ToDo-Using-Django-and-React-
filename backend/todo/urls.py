from unicodedata import name
from xml.etree.ElementInclude import include
from django.urls import path
from rest_framework import routers
from .views import TodoView

router = routers.DefaultRouter()
router.register('todos', TodoView, basename='todo')

urlpatterns = [
] + router.urls
