import datetime
from django.core.management.base import NoArgsCommand

from user_metrics.models import Metric, MetricItem, MetricDay, MetricWeek
from user_metrics.utils import week_for_date

class Command(NoArgsCommand):
    help = "Aggregate Application Metrics"

    requires_model_validation = True

    def handle_noargs(self, **options):
        """ Aggregate Metrics by User """

        # Aggregate Items
        items = MetricItem.objects.all()

        for item in items:
            # Daily Aggregation
            day, create = MetricDay.objects.get_or_create(
                metric = item.metric,
                user = item.user,
                date_up = item.date_up,
                user_object_id = item.user_object_id
            )

            day.count = day.count + item.count

            if item.last_visit is None or item.last_visit.date == datetime.date.today():
                day.unique_count = day.unique_count + item.count

            day.save()

            # Weekly Aggregation
            week_date = week_for_date(item.date_up)
            week, create = MetricWeek.objects.get_or_create(
                metric = item.metric,
                user = item.user,
                date_up = week_date,
                user_object_id = item.user_object_id
            )

            week.count = week.count + item.count

            if item.last_visit is None or (item.last_visit.date >= week_date and item.last_visit.date < week_date + datetime.timedelta(weeks=1)):
                day.unique_count = day.unique_count + item.count

            week.save()

        # Kill off our items
        items.delete()
