from user_metrics.models import MetricItem, MetricDay

from django.core.management.base import NoArgsCommand
from django.db.models.aggregates import Count
import datetime

class Command(NoArgsCommand):
    help = "Aggregate Application Metrics"

    requires_model_validation = True

    def handle_noargs(self, **options):
        """ Aggregate Metrics by User """

        items = MetricItem.objects.extra(
                select={'day': "DATE_TRUNC('day', visit_time)"}
            ).values('day', 'metric', 'user', 'user_object_id').order_by().annotate(
                    count=Count('id'), unique_count=Count('visitor_id', distinct=True))

        for item in items:
            day, create = MetricDay.objects.get_or_create(
                date_up = item['day'].date(),
                metric_id = item['metric'],
                user_id = item['user'],
                user_object_id = item['user_object_id']
            )

            day.count = item['count']
            day.unique_count = item['unique_count']

            day.save()

        MetricItem.objects.filter(visit_time__lt=datetime.date.today()).delete()
