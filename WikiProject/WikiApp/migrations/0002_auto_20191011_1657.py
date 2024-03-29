# Generated by Django 2.0.6 on 2019-10-11 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WikiApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainwikimodel',
            name='mainForeignKey',
        ),
        migrations.AddField(
            model_name='relatedwikimodel',
            name='mainForeignKey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='WikiApp.MainWikiModel'),
        ),
        migrations.AlterField(
            model_name='mainwikimodel',
            name='userForeignKey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
