from .models import ViewCount
from django.utils.deprecation import MiddlewareMixin
import re

class ViewCounterMiddleware(MiddlewareMixin):

    def process_request(self, request):
        """
        инкремент счетчика моделей
        :param request: 
        :return: 
        """
        if check_request_for_count(request.path):
            updated_view, created_view = ViewCount.objects.get_or_create(uri=request.path,
                                                                         defaults={'counter': 1,
                                                                                   'uri': request.path,
                                                                                   'model': 'default'})
            if updated_view:
                updated_view.counter = updated_view.counter + 1
                updated_view.uri = request.path
                updated_view.save()



def check_request_for_count(url):
    patterns = (
        r'^/gdz/\d+/[-a-z0-9]+/[-a-z0-9]+$',
        r'^/textbook/[-a-z0-9]+/[-a-z0-9]/[-a-z0-9]+$',
        r'^/writing/\d+/[-a-z0-9]+/[-a-z0-9]+$',
        r'^/library/[-a-z0-9]+/[-a-z0-9]+$',
        r'^/knowall/[-a-z0-9]+/[-a-z0-9]+$',
    )

    for pattern in patterns:
        if re.match(pattern, url):
            return True

    return False