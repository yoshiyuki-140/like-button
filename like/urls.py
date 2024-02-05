# coding:utf-8
from rest_framework import routers
from like.views import ObjectViewSet, object_detail
from django.urls import path

router = routers.DefaultRouter()
router.register('objects', ObjectViewSet)


urlpatterns = [
    path('objects/<int:object_id>/', object_detail, name='object_detail'),
]
