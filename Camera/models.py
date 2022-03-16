from django.db import models
from TLCam.settings import BASE_DIR
import os

# Create your models here.

class TLProject(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    interval = models.IntegerField(blank=False)
    status = models.BooleanField(default=False)
    project_path = models.CharField(max_length=255, default='', blank=True)
    frames_shot = models.IntegerField(default=0)
    slug = models.SlugField(blank=True)
    
    def __str__(self):
        return self.name

    def save(self):
        if self.slug == '':
            self.slug = self.name.replace(' ', '-')

        if not  os.path.exists(os.path.join(BASE_DIR, self.name)):
            os.mkdir(os.path.join(BASE_DIR, self.name))
            self.project_path = os.path.join(BASE_DIR, self.name)
        """
        if TLProject.objects.filter(status = True).exists():
            for x in TLProject.objects.filter(status = True):
                x.status = False
                x.save()
        """
        super(TLProject, self).save()
