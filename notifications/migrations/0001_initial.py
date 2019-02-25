# Generated by Django 2.1.3 on 2019-03-05 12:30

from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields
import notifications.enums
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', enumfields.fields.EnumField(enum=notifications.enums.NotificationType, max_length=50, unique=True, verbose_name='type')),
            ],
            options={
                'verbose_name': 'notification',
                'verbose_name_plural': 'notifications',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='NotificationTemplateTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('subject', models.CharField(max_length=255, verbose_name='subject')),
                ('body_html', models.TextField(blank=True, verbose_name='body, HTML version')),
                ('body_text', models.TextField(blank=True, help_text='If left blank, the HTML version without HTML tags will be used.', verbose_name='body, plain text version')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='notifications.NotificationTemplate')),
            ],
            options={
                'verbose_name': 'notification Translation',
                'db_table': 'notifications_notificationtemplate_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
            },
        ),
        migrations.AlterUniqueTogether(
            name='notificationtemplatetranslation',
            unique_together={('language_code', 'master')},
        ),
    ]
