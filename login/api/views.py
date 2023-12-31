from base64 import b64decode
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from .serializers import *
from rest_framework.response import Response
import jwt, datetime

class UserRegister(APIView):
    def post(self, request):
        serializer = UsuarioRegistroSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class UserLogin(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        
        user = Usuario.objects.filter(username=username).first()
        if user is None:
            raise AuthenticationFailed('Usuario no encontrado')
        if not user.check_password(password):
            raise AuthenticationFailed('contraseña incorrecta')
        
        now = datetime.datetime.utcnow()
        expiration = now + datetime.timedelta(minutes=60)
        payload = {
            'username': user.username,
            'cargo': user.cargo.cargo,
            'nombre': user.nombre,
            'apellido': user.apellido,
            'exp': int(expiration.timestamp()),
            'lat': int(now.timestamp())
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response
        
class UserView(APIView):
    def get(self, request):
        jwt_options = {
        'verify_signature': False,
        'verify_exp': True,
        'verify_nbf': False,
        'verify_iat': True,
        'verify_aud': False
        }
        token = request.COOKIES.get('jwt')
        print('token')
        if not token:
            raise AuthenticationFailed('No está autenticado')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'], options=jwt_options)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('No está autenticado')

        
        # Aquí puedes realizar las acciones adicionales que necesites con el usuario autenticado
        
        return Response({
            'username': payload['username'],
            'cargo': payload['cargo'],
            'nombre': payload['nombre'],
            'apellido': payload['apellido'],
        })
    
class UserLogout(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        
        return response