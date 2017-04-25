from .models import ViewCount
from django.utils.deprecation import MiddlewareMixin
from .tasks import incr_view_count

class ViewCounterMiddleware(MiddlewareMixin):

    def process_request(self, request):
        """
        инкремент счетчика моделей 
        """
        incr_view_count.delay(request.path)



