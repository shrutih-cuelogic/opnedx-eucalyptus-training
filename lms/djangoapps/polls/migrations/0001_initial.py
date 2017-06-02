# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference_name', models.CharField(max_length=200)),
                ('reference_type', models.CharField(default=b'', max_length=20, choices=[(b'Image', b'Image'), (b'Link', b'Link'), (b'Video', b'Video'), (b'Document', b'Document')])),
                ('reference_link', models.CharField(max_length=500)),
                ('reference_description', models.CharField(max_length=500)),
                ('reference_status', models.CharField(default=b'is_alive', max_length=20)),
            ],
        ),
    ]
