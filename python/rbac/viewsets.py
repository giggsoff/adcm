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

"""RBAC Permissions classes"""

from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, DjangoObjectPermissions


class DjangoModelPerm(DjangoModelPermissions):
    """
    Similar to `DjangoModelPermissions`, but adding 'view' permissions.
    """

    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
        'HEAD': ['%(app_label)s.view_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }


class DjangoOnlyObjectPermissions(DjangoObjectPermissions):
    perms_map = {
        'GET': [],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_permission(self, request, view):
        return True


class DjangoObjectPerm(DjangoObjectPermissions):
    """
    Similar to `DjangoObjectPermissions`, but adding 'view' permissions.
    """

    perms_map = {
        'GET': [],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    # def has_permission(self, request, view):
    #     if super().has_permission(request, view):
    #         return True
    #     else:
    #         queryset = self._queryset(view)
    #         perms = self.get_required_permissions(request.method, queryset.model)
    #         objects = get_objects_for_user(request.user, perms)
    #         if view.kwargs and objects.filter(
    #             **{view.lookup_field: view.kwargs[view.lookup_url_kwarg]}
    #         ):
    #             return True
    #     return False

    # def has_object_permission(self, request, view, obj):
    #     model_cls = self._queryset(view).model
    #     user = request.user
    #     model_perms = self.get_required_permissions(request.method, model_cls)
    #     object_perms = self.get_required_object_permissions(request.method, model_cls)
    #     if user.has_perms(object_perms, obj) or user.has_perms(model_perms):
    #         return True
    #     return False


class ModelPermViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """Replace of DRF ModelViewSet with view permission"""

    permission_classes = (DjangoObjectPerm,)
