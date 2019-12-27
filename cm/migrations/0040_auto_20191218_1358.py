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
# Generated by Django 2.2.6 on 2019-12-18 13:58
# pylint: disable=line-too-long

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0039_auto_20191203_0909'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.PositiveIntegerField(default=0)),
                ('title', models.TextField()),
                ('message', models.TextField()),
                ('result', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='prototypeconfig',
            name='type',
            field=models.CharField(choices=[('string', 'string'), ('text', 'text'), ('password', 'password'), ('json', 'json'), ('integer', 'integer'), ('float', 'float'), ('option', 'option'), ('boolean', 'boolean'), ('file', 'file'), ('list', 'list'), ('map', 'map'), ('structure', 'structure'), ('group', 'group')], max_length=16),
        ),
        migrations.AlterField(
            model_name='stageprototypeconfig',
            name='type',
            field=models.CharField(choices=[('string', 'string'), ('text', 'text'), ('password', 'password'), ('json', 'json'), ('integer', 'integer'), ('float', 'float'), ('option', 'option'), ('boolean', 'boolean'), ('file', 'file'), ('list', 'list'), ('map', 'map'), ('structure', 'structure'), ('group', 'group')], max_length=16),
        ),
    ]
