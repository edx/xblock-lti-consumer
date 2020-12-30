# Generated by Django 2.2.16 on 2020-10-24 11:47
from django.db import migrations, models

import lti_consumer


class Migration(migrations.Migration):

    dependencies = [
        ('lti_consumer', '0003_ltiagsscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='lticonfiguration',
            name='lti_1p3_internal_private_key',
            field=models.TextField(blank=True, help_text="Platform's generated Private key. Keep this value secret."),
        ),
        migrations.AddField(
            model_name='lticonfiguration',
            name='lti_1p3_internal_private_key_id',
            field=models.CharField(blank=True, help_text="Platform's generated Private key ID", max_length=255),
        ),
        migrations.AddField(
            model_name='lticonfiguration',
            name='lti_1p3_internal_public_jwk',
            field=models.TextField(blank=True, help_text="Platform's generated JWK keyset."),
        ),
        migrations.AddField(
            model_name='lticonfiguration',
            name='lti_1p3_client_id',
            field=models.CharField(default=lti_consumer.models.generate_client_id, help_text='Client ID used by LTI tool', max_length=255),
        ),
    ]