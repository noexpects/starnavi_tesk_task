from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

User = get_user_model()


class UserLastRequestTimeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            User.objects.filter(pk=request.user.id).update(last_request_time=timezone.now())
