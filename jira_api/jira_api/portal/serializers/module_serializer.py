from portal.models.module import Module
from rest_framework import serializers


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['name', 'project', 'status', 'due_date', 'started_on']