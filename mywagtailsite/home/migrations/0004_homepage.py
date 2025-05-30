# Generated by Django 5.2.1 on 2025-05-31 15:24

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_blogindexpage_blogpage_delete_homepage"),
        ("wagtailcore", "0094_alter_page_locale"),
        ("wagtailimages", "0027_image_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomePage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "hero_text",
                    models.CharField(
                        blank=True,
                        help_text="Text to display in the hero section of the homepage",
                        max_length=255,
                    ),
                ),
                (
                    "hero_cta",
                    models.CharField(
                        blank=True,
                        help_text="Call to action text for the hero section of the homepage",
                        max_length=255,
                        verbose_name="Hero Call to Action",
                    ),
                ),
                (
                    "body",
                    wagtail.fields.RichTextField(
                        blank=True, help_text="Content to display on the homepage"
                    ),
                ),
                (
                    "hero_cta_link",
                    models.ForeignKey(
                        blank=True,
                        help_text="Choose a page to link the hero call to action button to",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.page",
                        verbose_name="Hero Call to Action Link",
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        help_text="Homepage image",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
