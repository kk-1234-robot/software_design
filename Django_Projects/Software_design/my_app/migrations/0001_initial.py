# Generated by Django 5.1.4 on 2024-12-23 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case1', models.TextField()),
                ('case2', models.TextField()),
                ('case3', models.TextField()),
            ],
        ),
    ]