# Generated by Django 2.1.4 on 2019-10-24 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('institute', models.CharField(max_length=255)),
                ('dept', models.CharField(max_length=255)),
                ('aor', models.TextField()),
                ('phone', models.TextField()),
                ('web', models.URLField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
