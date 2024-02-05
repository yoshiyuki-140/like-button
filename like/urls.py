# coding:utf-8
from rest_framework import routers
from like.views import ObjectViewSet

router = routers.DefaultRouter()
router.register('objects', ObjectViewSet)
