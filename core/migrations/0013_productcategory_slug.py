# Generated by Django 3.0.5 on 2020-12-27 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_product_tag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]