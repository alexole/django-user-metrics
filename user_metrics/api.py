from user_metrics.models import Metric, MetricItem
from user_metrics.utils import get_visitor_hash, create_visitor_id

from django.http import HttpResponseRedirect

import datetime

VISITOR_ID_COOKIE = 'x-Arendorium-ID'

def put_metric(slug, user, user_object_id=0, request=None, response=None, cookie_domain=None, **kwargs):
    """ Increment a metric by a given user """

    try:
        metric = Metric.objects.get(slug=slug)
    except Metric.DoesNotExist:
        metric = Metric.objects.create(slug=slug, name=slug)

    visitor_hash = None
    visitor_id = None

    if request is not None and response is not None:
        # NOTE: expiring old cookies; the following loop can be removed in future
        for name, value in request.COOKIES.iteritems():
            if name.startswith('x-Arendorium-') and name != VISITOR_ID_COOKIE:
                response.set_cookie(name, '', expires=datetime.date(2010, 1, 1), domain=cookie_domain)

        visitor_hash = get_visitor_hash(request)

        visitor_id = request.COOKIES.get(VISITOR_ID_COOKIE, None)
        if visitor_id is None:
            visitor_id = create_visitor_id(request, visitor_hash)
            utcnow = datetime.datetime.utcnow()
            expires = utcnow.replace(year=utcnow.year+1)

            response.set_cookie(VISITOR_ID_COOKIE, value=visitor_id, expires=expires, domain=cookie_domain)

    MetricItem.objects.create(
        metric = metric,
        user = user,
        user_object_id = user_object_id,
        visitor_hash = visitor_hash,
        visitor_id = visitor_id
    )

    return response
