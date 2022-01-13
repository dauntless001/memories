from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from accounts.api.serializers import LoginSerializer
from django.contrib.auth import authenticate


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        data = {}
        if request.data:
            username = request.data['username']
            password = request.data['password']
            user = authenticate(request, username=username, password=password)
            data['message'] = 'Invalid Login credentials, Check and Try again'
            if user is not None:
                data['token'] = f'{user.auth_token}'
                data['message'] = 'Login safely'
            return Response(data)
            