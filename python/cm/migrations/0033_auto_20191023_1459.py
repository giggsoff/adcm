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

# Generated by Django 2.2.4 on 2019-10-23 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0032_auto_20191015_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundle',
            name='edition',
            field=models.CharField(default='community', max_length=80),
        ),
        migrations.AddField(
            model_name='stageprototype',
            name='edition',
            field=models.CharField(default='community', max_length=80),
        ),
        migrations.AddField(
            model_name='stageupgrade',
            name='from_edition',
            field=models.TextField(blank=True, default='[\"community\"]'),
        ),
        migrations.AddField(
            model_name='upgrade',
            name='from_edition',
            field=models.TextField(blank=True, default='[\"community\"]'),
        ),
        migrations.AlterUniqueTogether(
            name='bundle',
            unique_together={('name', 'version', 'edition')},
        ),
    ]
