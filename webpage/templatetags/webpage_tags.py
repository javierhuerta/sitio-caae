from django import template
from webpage.models import Menu

register = template.Library()

# Advert snippets
@register.inclusion_tag('webpage/tags/menu.html', takes_context=True)
def navbar_menu(context):
  return {
    'menus': Menu.objects.all().order_by('order'),
    'request': context['request'],
  }