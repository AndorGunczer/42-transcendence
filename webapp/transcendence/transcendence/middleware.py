# This file is used to define middleware classes. Middleware is a way to process requests 
#     globally before they reach the view or after the view has processed them.


from django.utils.deprecation import MiddlewareMixin

class JWTAuthFromCookiesMiddleware(MiddlewareMixin):
    def process_request(self, request):
        access_token = request.COOKIES.get('access_token')
        if access_token:
            request.META['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'