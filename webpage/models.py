from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet


class AboutPage(Page):
    sub_title = models.CharField(max_length=255)
    body = RichTextField()

AboutPage.content_panels = [
    FieldPanel('title', classname="Title"),
    FieldPanel('sub_title', classname="Sub Title"),
    FieldPanel('body', classname="Content")
]


@register_snippet
class Team(models.Model):
    name = models.CharField(max_length=255)
    function = models.CharField(max_length=255)
    description = RichTextField(null=True, blank=True)
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('function'),
        FieldPanel('description'),
        ImageChooserPanel('photo'),
        ]

    def __unicode__(self):
        return u"%s" % self.name

class TeamPageTeamList(Orderable, models.Model):
    page = ParentalKey('webpage.TeamPage', related_name='team_list')
    team = models.ForeignKey('webpage.Team', related_name='+')

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"

    panels = [
        SnippetChooserPanel('team', Team),
        ]

    def __unicode__(self):
        return u"%s -> %s" % (self.page.title,self.team)

class TeamPage(Page):
    pass

TeamPage.content_panels = [
    FieldPanel('title', classname="Title"),
    InlinePanel(TeamPage,'team_list', label="Teams")
]

class ContactPage(Page):
    subtitle = models.CharField(max_length=255)
    description = RichTextField()

ContactPage.content_panels = [
    FieldPanel('title'),
    FieldPanel('subtitle'),
    FieldPanel('description'),
]

####MENU NAVIGATION##################3
class LinkFields(models.Model):
    """
    Represents a link to an external page, a document or a Wagtail page
    """
    link_external = models.URLField(
        "External link",
        blank=True,
        null=True,
        help_text='Set an external link if you want the link to point somewhere outside the CMS.'
    )
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        related_name='+',
        help_text='Choose an existing page if you want the link to point somewhere inside the CMS.'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        related_name='+',
        help_text='Choose an existing document if you want the link to open a document.'
    )

class MenuItem(LinkFields):

    @property
    def url(self):
        if self.link_external:
            return self.link
        elif self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document.url

    def __unicode__(self):
        if self.link_external:
            title = self.link_external
        elif self.link_page:
            title = self.link_page.title
        elif self.link_document:
            title = self.link_document.title
        return title

    class Meta:
        verbose_name = "Menu item"

class MenuMenuItem(Orderable, MenuItem):
    parent = ParentalKey(to='webpage.Menu', related_name='menu_items')

class MenuManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(menu_name=name)

@register_snippet
class Menu(models.Model):
    objects = MenuManager()
    menu_name = models.CharField(max_length=255, null=False, blank=False)

    @property
    def items(self):
        return self.menu_items.all()

    def __unicode__(self):
        return self.menu_name

    class Meta:
        verbose_name = "Navigation menu"

Menu.panels = [
    FieldPanel('menu_name', classname='full title'),
    InlinePanel(Menu, 'menu_items', label="Menu Items", help_text='Set the menu items for the current menu.')
]
#############################################################################################################