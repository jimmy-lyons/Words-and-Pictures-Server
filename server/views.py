from django.http import JsonResponse 
from .models import Project, ProjectImage
from .serializers import ProjectSerializer, ImageSerializer

def project_list(request):
  projects = Project.objects.all()
  serializer = ProjectSerializer(projects, many=True)
  return JsonResponse(serializer.data, safe=False)

def project_images(request):
  images = ProjectImage.objects.filter(projectId=1)
  serializer = ImageSerializer(images, many=True)
  return JsonResponse(serializer.data, safe=False)
  