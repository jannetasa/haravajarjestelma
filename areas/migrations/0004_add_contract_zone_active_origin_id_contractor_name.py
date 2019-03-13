# Generated by Django 2.1.3 on 2019-03-11 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('areas', '0003_add_contract_zone_contractor'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractzone',
            name='active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
        migrations.RenameField(
            model_name='contractzone',
            old_name='contractor',
            new_name='contractor_user',
        ),
        migrations.AlterField(
            model_name='contractzone',
            name='contractor_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contract_zones', to=settings.AUTH_USER_MODEL, verbose_name='contractor user'),
        ),
        migrations.AddField(
            model_name='contractzone',
            name='origin_id',
            field=models.CharField(max_length=50, unique=True, verbose_name='origin ID'),
        ),
        migrations.AddField(
            model_name='contractzone',
            name='contractor',
            field=models.CharField(blank=True, max_length=255, verbose_name='contractor'),
        ),
    ]
