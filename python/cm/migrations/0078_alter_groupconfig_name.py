# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by Django 3.2.6 on 2021-10-25 07:31

from django.db import migrations, models

import cm.models


def remove_line_break_character(apps, schema_editor):
    """Remove line break character from `name` field from `GroupConfig` model"""
    GroupConfig = apps.get_model('cm', 'GroupConfig')
    for gc in GroupConfig.objects.all():
        gc.name = ''.join(gc.name.splitlines())
        gc.save()


class Migration(migrations.Migration):
    dependencies = [
        ('cm', '0077_job_lock_message_tpl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupconfig',
            name='name',
            field=models.CharField(
                max_length=30, validators=[cm.models.validate_line_break_character]
            ),
        ),
        migrations.RunPython(remove_line_break_character),
    ]