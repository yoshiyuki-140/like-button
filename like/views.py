# coding:utf-8
from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters


from like.models import Object
from like.serializer import ObjectSerializer


class ObjectViewSet(viewsets.ModelViewSet):
    """ViewSet for the Object class
    """
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer


def index(request):
    return render(request, 'index.html', {})
