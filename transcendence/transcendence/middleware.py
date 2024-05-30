# middleware.py
from django.utils.deprecation import MiddlewareMixin

class JWTAuthFromCookiesMiddleware(MiddlewareMixin):
    def process_request(self, request):
        access_token = request.COOKIES.get('access_token')
        if access_token:
            request.META['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'