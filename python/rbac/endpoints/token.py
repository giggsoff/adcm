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

"""View and serializer for Authentication token"""

import django.contrib.auth

import rest_framework
import rest_framework.authtoken.serializers
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from adwp_base.errors import AdwpEx


class AuthSerializer(rest_framework.authtoken.serializers.AuthTokenSerializer):
    """Authentication token serializer"""

    def validate(self, attrs):
        user = django.contrib.auth.authenticate(
            username=attrs.get('username'), password=attrs.get('password')
        )
        if not user:
            raise AdwpEx('AUTH_ERROR', 'Wrong user or password')
        attrs['user'] = user
        return attrs


class GetAuthToken(GenericAPIView):
    """Authentication token view"""

    authentication_classes = (rest_framework.authentication.TokenAuthentication,)
    permission_classes = (rest_framework.permissions.AllowAny,)
    serializer_class = AuthSerializer

    def post(self, request, *args, **kwargs):
        """
        Provide authentication token

        HTTP header for authorization:

        ```Authorization: Token XXXXX```
        """
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _created = Token.objects.get_or_create(user=user)
        django.contrib.auth.login(
            request, user, backend='django.contrib.auth.backends.ModelBackend'
        )
        return Response({'token': token.key})