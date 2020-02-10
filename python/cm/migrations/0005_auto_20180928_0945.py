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
# Generated by Django 2.0.5 on 2018-09-28 09:45
# pylint: disable=line-too-long

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0004_auto_20180914_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='prototypeconfig',
            name='action',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cm.Action'),
        ),
        migrations.AddField(
            model_name='stageprototypeconfig',
            name='action',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cm.StageAction'),
        ),
        migrations.AddField(
            model_name='tasklog',
            name='config',
            field=models.TextField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='prototypeconfig',
            unique_together={('prototype', 'action', 'name', 'subname')},
        ),
        migrations.AlterUniqueTogether(
            name='stageprototypeconfig',
            unique_together={('prototype', 'action', 'name', 'subname')},
        ),
    ]