import datetime
from datetime import date
from django.db import models
from django.contrib.auth.models import User

class Metric(models.Model):
    """ holds the types of metrics
    """
    slug = models.SlugField(unique=True, max_length=100, db_index=True)
    name = models.CharField(max_length=90)

    def __unicode__(self): return self.name


class MetricItem(models.Model):
    """ more atomic representation of a metric by each user
    """
    metric = models.ForeignKey(Metric)
    user = models.ForeignKey(User)

    user_object_id = models.IntegerField(default=0)

    count = models.IntegerField(default=1)
    date_up = models.DateField(default=date.today)

    last_visit = models.DateField(null=True)

    def __unicode__(self):
        return '%d %s by %s at %s, object: %s' % (self.count, self.metric.name, self.user, self.date_up, self.user_object_id)


class MetricDay(models.Model):
    """ represent aggregation of metrics daily
    """
    metric = models.ForeignKey(Metric)
    user = models.ForeignKey(User)
    user_object_id = models.IntegerField(default=0)

    count = models.IntegerField(default=0)
    unique_count = models.IntegerField(default=0)
    date_up = models.DateField(default=date.today)


class MetricWeek(models.Model):
    """ represent aggregation of metric weekly
    """
    metric = models.ForeignKey(Metric)
    user = models.ForeignKey(User)
    user_object_id = models.IntegerField(default=0)

    count = models.IntegerField(default=0)
    unique_count = models.IntegerField(default=0)
    date_up = models.DateField(default=date.today)
