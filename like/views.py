# coding:utf-8
from django.shortcuts import render
from rest_framework import viewsets


from like.models import Object
from like.serializer import ObjectSerializer


class ObjectViewSet(viewsets.ModelViewSet):
    """ViewSet for the Object class
    """
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer


def index(request):
    '''トップページのビュー
    '''
    return render(request, 'index.html', {'objects': Object.objects.all()})


def object_detail(request, object_id):
    '''オブジェクトの詳細ページのビュー
    '''
    return render(request, 'object_detail.html', {'object': Object.objects.get(id=object_id)})
