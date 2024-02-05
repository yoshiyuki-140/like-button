# coding : utf-8

from rest_framework import serializers
from like.models import Object


class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = '__all__'
