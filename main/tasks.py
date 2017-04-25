from celery import task
import re

from .models import ViewCount

@task()
def incr_view_count(path):
    if check_request_for_count(path):
        updated_view, created_view = ViewCount.objects.get_or_create(uri=path,
                                                                     defaults={'counter': 1,
                                                                               'uri': path,
                                                                               'model': 'default'})
        if updated_view:
            updated_view.counter = updated_view.counter + 1
            updated_view.uri = path
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