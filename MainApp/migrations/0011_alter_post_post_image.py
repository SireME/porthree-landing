# Generated by Django 4.2.7 on 2023-12-13 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MainApp", "0010_post_post_image_alter_post_content_alter_post_like_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="post_image",
            field=models.ImageField(blank=True, null=True, upload_to="post_images/"),
        ),
    ]
