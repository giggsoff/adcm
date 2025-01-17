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

# Generated by Django 2.2.1 on 2019-06-24 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0022_auto_20190620_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='prototype',
            name='adcm_min_version',
            field=models.CharField(default=None, null=True, max_length=80),
        ),
        migrations.AddField(
            model_name='prototypeconfig',
            name='ui_options',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='stageprototype',
            name='adcm_min_version',
            field=models.CharField(default=None, null=True, max_length=80),
        ),
        migrations.AddField(
            model_name='stageprototypeconfig',
            name='ui_options',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
