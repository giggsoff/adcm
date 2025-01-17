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

# Generated by Django 2.1.7 on 2019-08-13 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0027_auto_20190809_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='prototypeimport',
            name='required',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stageprototypeimport',
            name='required',
            field=models.BooleanField(default=False),
        ),
    ]
