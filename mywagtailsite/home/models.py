from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.search import index
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

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

class HomePage(Page):
    
    image = models.ForeignKey(
        "wagtailimages.Image", # ForeignKey to Wagtail's Image model
        null=True, # Allow null values
        blank=True, # Allow blank values
        on_delete=models.SET_NULL, # If the image is deleted, set this field to null
        related_name="+", # No reverse relation needed, improves performance when reverse lookups are not required.
        # In other words, you’re instructing Django to create a way to access wagtailimages.Image
        # from your Homepage but not a way to access HomePage from wagtailimages.Image.
        help_text="Homepage image", # Help text for the admin interface
    )
    # The image field is a ForeignKey referencing Wagtails built in image model for storing images.
    
    hero_text = models.CharField(
        max_length = 255,
        blank=True,
        help_text="Text to display in the hero section of the homepage",
    )
    
    hero_cta = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Hero Call to Action", # Verbose name for the admin interface
        help_text="Call to action text for the hero section of the homepage",
    )
    
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page", # ForeignKey to Wagtail's Page model
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero Call to Action Link",
        help_text="Choose a page to link the hero call to action button to",
    )
    # The wagtailcore.Page model is the base model for all Wagtail pages,
    # allowing you to link to any page in your Wagtail site within the CMS.
    
    body = RichTextField(
        blank=True,
        help_text="Content to display on the homepage",
    )
    
    # Add the content panels to the admin interface
    content_panels= Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("image"),
                FieldPanel("hero_text"),
                FieldPanel("hero_cta"),
                FieldPanel("hero_cta_link"),
            ],
            heading="Hero Section",
        ),
        FieldPanel("body"),
    ]