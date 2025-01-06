# Generated by Django 5.1.4 on 2025-01-05 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_sentences_pos_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='words',
            name='article_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='words',
            name='pos_index',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='words',
            name='sentence_id',
            field=models.IntegerField(default=0),
        ),
    ]
