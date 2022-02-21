from dataclasses import field
from rest_framework import serializers
from .models import Task

class TaskSerializrers(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields       ='__all__'