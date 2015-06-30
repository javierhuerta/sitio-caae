from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, InlinePanel,
    MultiFieldPanel)
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField

class HomePage(Page):
    about_text = RichTextField()
    about_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        related_name='about_+',
        help_text='Choose the about page'
    )
    programs_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        related_name='about_+',
        help_text='Choose the programs page'
    )
    gallery_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        related_name='gallery_+',
        help_text='Choose the gallery page'
    )
    news_description = RichTextField(null=True, blank=True)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    facebook = models.URLField(null=True, blank=True)
    twiter = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)

    def get_context(self, request):
        programs = Program.objects.order_by('?')[:3]
        images = PictureGallery.objects.all()
        slides = Slide.objects.order_by('pk')
        talleres = TallerPage.objects.all()[:9]
        news = New.objects.order_by('-created_at')[:6]

        # Update template context
        context = super(HomePage, self).get_context(request)
        context['programs'] = programs
        context['images'] = images
        context['slides'] = slides
        context['talleres'] = talleres
        context['news_one'] = news[:3]
        context['news_two'] = news[3:6]
        return context

    @property
    def images_gallery(self):
        return PictureGallery.objects.order_by('?')[:6]

HomePage.content_panels = [
    FieldPanel('title', classname="Title"),
    FieldPanel('about_text', classname="About Text"),
    FieldPanel('about_page', classname="About Page"),
    FieldPanel('programs_page', classname="Programs Page"),
    FieldPanel('gallery_page', classname="Gallery Page"),
    FieldPanel('phone', classname="Phone"),
    FieldPanel('address', classname="Address"),
    FieldPanel('email', classname="Email"),
    FieldPanel('facebook', classname="Facebook"),
    FieldPanel('twiter', classname="Twiter"),
    FieldPanel('instagram', classname="Instagram"),

]

class AboutPage(Page):
    sub_title = models.CharField(max_length=255)
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = RichTextField()
    body_personalize = models.TextField(null=True, blank=True)

AboutPage.content_panels = [
    FieldPanel('title', classname="Title"),
    FieldPanel('sub_title', classname="Sub Title"),
    FieldPanel('body', classname="Content"),
    FieldPanel('body_personalize', classname="Content Personalize"),
    ImageChooserPanel('photo'),
]

@register_snippet
class Person(models.Model):
    name = models.CharField(max_length=255)
    mail = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s" % self.name

class PersonList(Orderable, models.Model):
    page = ParentalKey('webpage.TallerPage', related_name='person_list')
    person = models.ForeignKey('webpage.Person', related_name='+')

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

    panels = [
        SnippetChooserPanel('person', Person),
        ]

    def __unicode__(self):
        return u"%s -> %s" % (self.page.title,self.person)

class TallerPage(Page):
    name = models.CharField(max_length=255,
        null=True,
        blank=True
    )
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    team = models.ForeignKey('Team',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    time = models.CharField(max_length=255)
    date = models.DateField()
    room = models.CharField(max_length=255)
    number = models.PositiveIntegerField()
    body = RichTextField()

TallerPage.content_panels = [
    FieldPanel('title', classname="Title"),
    FieldPanel('name', classname="Name"),
    FieldPanel('team', classname="Instructor"),
    FieldPanel('time', classname="Time"),
    FieldPanel('date', classname="Date"),
    FieldPanel('room', classname="Room"),
    FieldPanel('number', classname="Number"),
    FieldPanel('body', classname="Content"),
    ImageChooserPanel('photo'),
    InlinePanel(TallerPage,'person_list', label="Persons")
]

class DefaultPage(Page):
    body = RichTextField()

DefaultPage.content_panels = [
    FieldPanel('title', classname="Title"),
    FieldPanel('body', classname="Content"),
]

@register_snippet
class Program(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField(null=True, blank=True)
    short_description = RichTextField(null=True, blank=True)
    icon_class = models.CharField(max_length=255, blank=True, null=True)
    related_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        related_name='gallery_+',
        help_text='Select a page related'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s" % self.name


@register_snippet
class PictureGallery(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField(null=True, blank=True)
    program = models.ForeignKey(Program)
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('program'),
        ImageChooserPanel('photo'),
        ]

    def __unicode__(self):
        return u"%s" % self.title

class GalleryPagePictureList(Orderable, models.Model):
    page = ParentalKey('webpage.GalleryPage', related_name='picture_list')
    picture = models.ForeignKey('webpage.PictureGallery', related_name='+')

    class Meta:
        verbose_name = "Picture"
        verbose_name_plural = "Pictures"

    panels = [
        SnippetChooserPanel('picture', PictureGallery),
        ]

    def __unicode__(self):
        return u"%s -> %s" % (self.page.title, self.picture)

class GalleryPage(Page):
    pass

    def get_context(self, request):
        # Get progrmas
        programs = Program.objects.all()

        # Update template context
        context = super(GalleryPage, self).get_context(request)
        context['programs'] = programs
        return context

GalleryPage.content_panels = [
    FieldPanel('title', classname="Title"),
    InlinePanel(GalleryPage,'picture_list', label="Pictures")
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

class FormField(AbstractFormField):
    page = ParentalKey('ContactPage', related_name='form_fields')

class ContactPage(AbstractEmailForm):
    subtitle = models.CharField(max_length=255)
    description = RichTextField()

ContactPage.content_panels = [
    FieldPanel('title'),
    FieldPanel('subtitle'),
    FieldPanel('description'),
    InlinePanel(ContactPage, 'form_fields', label="Form fields"),
    MultiFieldPanel([
        FieldPanel('to_address', classname="full"),
        FieldPanel('from_address', classname="full"),
        FieldPanel('subject', classname="full"),
    ], "Email")
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
    menu = models.ForeignKey(
        'webpage.Menu',
        blank=True,
        null=True
    )

class MenuItem(LinkFields):

    @property
    def url(self):
        if self.link_external:
            return self.link_external
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
    second_level = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=1)

    @property
    def items(self):
        return self.menu_items.all()

    def __unicode__(self):
        return self.menu_name

    class Meta:
        verbose_name = "Navigation menu"

Menu.panels = [
    FieldPanel('menu_name', classname='full title'),
    FieldPanel('second_level', classname="Is Second Level"),
    FieldPanel('order', classname="Order"),
    InlinePanel(Menu, 'menu_items', label="Menu Items", help_text='Set the menu items for the current menu.')
]
#############################################################################################################

####SLIDER######
@register_snippet
class Slide(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField(null=True, blank=True)
    order = models.PositiveIntegerField(default=1)
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
        FieldPanel('description'),
        FieldPanel('order'),
        ImageChooserPanel('photo'),
        ]

    def __unicode__(self):
        return u"%s" % self.name

##NEWS#######

@register_snippet
class New(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User)
    description = RichTextField()
    short_description = RichTextField(null=True, blank=True)
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('author'),
        FieldPanel('description'),
        FieldPanel('short_description'),
        ImageChooserPanel('photo'),
        ]

    def __unicode__(self):
        return u"%s" % self.title

class NewList(Orderable, models.Model):
    page = ParentalKey('webpage.NewsPage', related_name='new_list')
    new = models.ForeignKey('webpage.New', related_name='+')

    class Meta:
        verbose_name = "New"
        verbose_name_plural = "News"

    panels = [
        SnippetChooserPanel('new', New),
        ]

    def __unicode__(self):
        return u"%s -> %s" % (self.page.title, self.new)

class NewsPage(Page):
    pass

    def get_context(self, request):
        news_list = self.new_list.order_by('-new__created_at')
        filter = request.GET.get('filter', None)
        if filter:
            news_list = news_list.filter(new__title__icontains=filter)

        paginator = Paginator(news_list, 4) # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            news = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            news = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            news = paginator.page(paginator.num_pages)

        # Update template context
        context = super(NewsPage, self).get_context(request)
        context['news'] = news
        return context

NewsPage.content_panels = [
    FieldPanel('title', classname="Title"),
    InlinePanel(NewsPage, 'new_list', label="News")
]

####PROGRAMS PAGE####

class ProgramsPage(Page):
    pass

    def get_context(self, request):
        programs = Program.objects.all()
        context = super(ProgramsPage, self).get_context(request)
        context['programs'] = programs
        return context

ProgramsPage.content_panels = [
    FieldPanel('title', classname="Title"),
]