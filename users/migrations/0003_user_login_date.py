# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 5, 8, 17, 40, 844638, tzinfo=utc), verbose_name='date login_date'),
            preserve_default=False,
        ),
    ]
