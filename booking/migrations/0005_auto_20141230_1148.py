# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import booking.models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20141230_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingsettings',
            name='display_permissions',
            field=models.BooleanField(default=False, help_text='Display permissions on the list of bookings.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='booking',
            name='permission',
            field=models.ForeignKey(to='booking.Permission', default=booking.models.default_permission),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bookingsettings',
            name='notes_user_staff',
            field=models.BooleanField(default=False, help_text='Allow a member of staff to edit notes for logged in users (and members of staff)'),
            preserve_default=True,
        ),
    ]