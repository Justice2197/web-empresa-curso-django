# Generated by Django 4.0.3 on 2022-03-04 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_mame_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='get_posts', to='blog.category', verbose_name='Categorías'),
        ),
    ]
