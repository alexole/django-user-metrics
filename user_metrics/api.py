from user_metrics.models import Metric, MetricItem

import datetime
import dateutil

# TODO: keep last visit date in DB for authenticated users
def put_metric(slug, user, user_object_id=0, count=1, request=None, response=None, cookie_domain=None, **kwargs):
    """ Increment a metric by a given user """

    try:
        metric = Metric.objects.get(slug=slug)
    except Metric.DoesNotExist:
        metric = Metric.objects.create(slug=slug, name=slug)

    cookie_name = 'x-Arendorium-{0}'.format(slug)

    if response is not None:
        utcnow = datetime.date.utcnow()
        utcnow_str = utcnow.strftime('%d-%b-%Y %H:%M:%S')

        response.set_cookie(
                cookie_name,
                value=utcnow_str,
                expires=utcnow + datetime.timedelta(years=1),
                domain=cookie_domain)

    last_visit = None

    if request is not None:
        last_visit_str = request.COOKIES.get(cookie_name, None)
        if last_visit_str is not None:
            try:
                last_visit = dateutil.tz.tzlocal().fromutc(datetime.strptime(last_visit_str, '%d-%b-%Y %H:%M:%S'))
            except ValueError:
                pass

    MetricItem.objects.create(
        metric = metric,
        user = user,
        user_object_id = user_object_id,
        count = count,
        last_visit = last_visit
    )
