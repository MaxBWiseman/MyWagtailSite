from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.search import index

class BlogIndexPage(Page):
    # Since the model name is BlogIndexPage, Wagtail will automatically associate the
    # template with the name blog_index_page.html (you must create this template in your templates directory
    # my_app/templates/my_app/).
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + ["intro"]


class BlogPage(Page):

    date = models.DateField(auto_now_add=True)
    intro = models.CharField(max_length=250, blank=True)
    body = RichTextField(blank=True)
    
    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("body"),
    ]
    
    content_panels = Page.content_panels + ["intro", "body"]