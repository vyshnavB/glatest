# Generated by Django 4.1.3 on 2022-12-08 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0027_post_page_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='page_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
