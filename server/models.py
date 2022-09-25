from distutils.command.upload import upload
from django.db import models


class Project(models.Model):
  name = models.CharField(max_length=200)
  heading = models.CharField(max_length=200, default="")
  client = models.CharField(max_length=200, default="")
  description = models.TextField(default="")

  def __str__(self):
    return self._id + ": " + self.name + " / " + self.heading


class ProjectImage(models.Model):
  name = models.CharField(max_length=200)
  projectId = models.ForeignKey(Project, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='images')

  def __str__(self):
    return self.name + ", " + self.project
