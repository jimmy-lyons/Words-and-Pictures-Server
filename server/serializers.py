from rest_framework import serializers
from .models import Project, ProjectImage

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ['id', 'name', 'heading', 'client', 'description']
    

class ImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProjectImage
    fields = ['id', 'projectId', 'image']
