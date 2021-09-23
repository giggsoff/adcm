# Generated by Django 3.2 on 2021-08-12 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0071_messagetemplate'),
    ]

    operations = [
        migrations.AddField(
            model_name='adcm',
            name='_multi_state',
            field=models.JSONField(db_column='multi_state', default=dict),
        ),
        migrations.AddField(
            model_name='cluster',
            name='_multi_state',
            field=models.JSONField(db_column='multi_state', default=dict),
        ),
        migrations.AddField(
            model_name='clusterobject',
            name='_multi_state',
            field=models.JSONField(db_column='multi_state', default=dict),
        ),
        migrations.AddField(
            model_name='host',
            name='_multi_state',
            field=models.JSONField(db_column='multi_state', default=dict),
        ),
        migrations.AddField(
            model_name='hostprovider',
            name='_multi_state',
            field=models.JSONField(db_column='multi_state', default=dict),
        ),
        migrations.AddField(
            model_name='servicecomponent',
            name='_multi_state',
            field=models.JSONField(db_column='multi_state', default=dict),
        ),
    ]