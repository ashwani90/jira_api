from portal.models.project import Project
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'client_name', 'budget', 'status', 'due_date', 'started_on', 'users']