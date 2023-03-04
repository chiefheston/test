from django import template
from django.utils.safestring import mark_safe
from ..models import *
from ..views import *

register = template.Library()


@register.simple_tag()
def draw_menu(name: str):
    html = ''
    queryset = Item.objects.all().values()
    for item in queryset:
        if item['name'] == name:
            html = f"<div><a href='menu/?id={item['id']}&name={item['name']}'>{item['name']}</a><div>"
    return mark_safe(html)