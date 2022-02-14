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

"""Group view sets"""

from adwp_base.errors import AdwpEx
from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_framework import serializers, status

from rbac import models
from rbac.services import group as group_services
from rbac.viewsets import ModelPermViewSet


class UserSerializer(serializers.Serializer):
    """Simple User serializer"""

    id = serializers.IntegerField()
    url = serializers.HyperlinkedIdentityField(view_name='rbac:user-detail')


class UserGroupSerializer(serializers.Serializer):
    """Simple Group serializer"""

    id = serializers.IntegerField()
    url = serializers.HyperlinkedIdentityField(view_name='rbac:group-detail')


class ExpandedUserSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    """Expanded User serializer"""

    group = UserGroupSerializer(many=True, source='groups')
    url = serializers.HyperlinkedIdentityField(view_name='rbac:user-detail')

    class Meta:
        model = models.User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_superuser',
            'group',
            'url',
        )
        expandable_fields = {
            'group': (
                'rbac.endpoints.group.views.GroupSerializer',
                {'many': True, 'source': 'groups'},
            )
        }


class GroupSerializer(FlexFieldsSerializerMixin, serializers.Serializer):
    """
    Group serializer
    Group model inherits 'user_set' property from parent class, which refers to 'auth.User',
    so it has not our custom properties in expanded fields
    """

    id = serializers.IntegerField(read_only=True)
    name = serializers.RegexField(r'^[^\n]+$', max_length=150)
    description = serializers.CharField(
        max_length=255, allow_blank=True, required=False, default=''
    )
    user = UserSerializer(many=True, required=False, source='user_set')
    url = serializers.HyperlinkedIdentityField(view_name='rbac:group-detail')
    built_in = serializers.BooleanField(read_only=True)

    class Meta:
        expandable_fields = {'user': (ExpandedUserSerializer, {'many': True, 'source': 'user_set'})}

    def update(self, instance, validated_data):
        return group_services.update(instance, partial=self.partial, **validated_data)

    def create(self, validated_data):
        return group_services.create(**validated_data)


class GroupViewSet(ModelPermViewSet):  # pylint: disable=too-many-ancestors
    """Group view set"""

    queryset = models.Group.objects.all()
    serializer_class = GroupSerializer
    filterset_fields = ('id', 'name')
    ordering_fields = ('id', 'name')
    search_fields = ('name', 'description')

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.built_in:
            raise AdwpEx(
                'GROUP_DELETE_ERROR',
                msg='Built-in group could not be deleted',
                http_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        return super().destroy(request, args, kwargs)