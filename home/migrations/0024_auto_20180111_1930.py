# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-11 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20180111_0200'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='no_proprietary_software',
            field=models.BooleanField(default=False, help_text='I assert that this Outreachy internship project will forward the interests of free and open source software, not proprietary software.'),
        ),
        migrations.AddField(
            model_name='project',
            name='proprietary_software_description',
            field=models.CharField(blank=True, help_text='(Optional) If this internship project furthers the interests of proprietary software, please explain.', max_length=3000),
        ),
        migrations.AddField(
            model_name='project',
            name='unapproved_license_description',
            field=models.CharField(blank=True, help_text='(Optional) If your community uses a license that is not an OSI-approved license or a Creative Commons license, please provide links to the licenses or a description.', max_length=3000),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='approved_license',
            field=models.BooleanField(help_text='I assert that all Outreachy internship projects under my community will be released under either an <a href="https://opensource.org/licenses/alphabetical">OSI-approved open source license</a> that is also identified by the FSF as a <a href="https://www.gnu.org/licenses/license-list.html">free software license</a>, OR a <a href="https://creativecommons.org/share-your-work/public-domain/freeworks/">Creative Commons license approved for free cultural works</a>'),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='no_proprietary_software',
            field=models.BooleanField(help_text='I assert all Outreachy internship projects under my community will forward the interests of free and open source software, not proprietary software.'),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='proprietary_software_description',
            field=models.CharField(blank=True, help_text='(Optional) If any internship project under your community furthers the interests of proprietary software, please explain.', max_length=3000),
        ),
        migrations.AlterField(
            model_name='participation',
            name='cfp_text',
            field=models.CharField(max_length=3000, verbose_name="Additional information to provide on a call for mentors and volunteers page (e.g. what kinds of internship projects you're looking for, ways for volunteers to help Outreachy applicants)"),
        ),
        migrations.AlterField(
            model_name='project',
            name='approved_license',
            field=models.BooleanField(help_text='I assert that Outreachy internship projects will released under either an <a href="https://opensource.org/licenses/alphabetical">OSI-approved open source license</a> that is also identified by the FSF as a <a href="https://www.gnu.org/licenses/license-list.html">free software license</a>, OR a <a href="https://creativecommons.org/share-your-work/public-domain/freeworks/">Creative Commons license approved for free cultural works</a>'),
        ),
    ]
