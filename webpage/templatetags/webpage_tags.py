from django import template
from webpage.models import Menu, HomePage

register = template.Library()

# Advert snippets
@register.inclusion_tag('webpage/tags/menu.html', takes_context=True)
def navbar_menu(context):
  return {
    'menus': Menu.objects.all().order_by('order'),
    'request': context['request'],
  }

@register.assignment_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    id = context['request'].site.root_page.id
    return HomePage.objects.get(id=id)
