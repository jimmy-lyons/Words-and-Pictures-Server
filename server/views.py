from django.http import JsonResponse 
from .models import Project, ProjectImage
from .serializers import ProjectSerializer, ImageSerializer
from rest_framework.decorators import api_view

def project_list(request):
  projects = Project.objects.all()
  serializer = ProjectSerializer(projects, many=True)
  return JsonResponse(serializer.data, safe=False)

@api_view(['POST',])
def project_images(request):
  data = request.data
  images = ProjectImage.objects.filter(projectId=data['id'])
  serializer = ImageSerializer(images, many=True)
  return JsonResponse(serializer.data, safe=False)
  