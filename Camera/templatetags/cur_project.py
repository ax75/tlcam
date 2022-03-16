from django import template
from Camera.models import TLProject

register = template.Library()

@register.simple_tag
def active_project():
    print(TLProject.objects.filter(status=True))
    return TLProject.objects.get(status=True) if TLProject.objects.filter(status=True).exists() else None
