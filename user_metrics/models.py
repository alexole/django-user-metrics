import datetime

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

    visit_time = models.DateTimeField(default=datetime.datetime.now)
    visitor_hash = models.CharField(max_length=22, null=True)
    visitor_id = models.CharField(max_length=22, null=True)

    def __unicode__(self):
        return '%s by %s at %s, object: %s, hash: %s, id: %s' % (
                self.metric.name,
                self.user,
                self.timestamp,
                self.user_object_id,
                self.visitor_hash,
                self.visitor_id)


class MetricDay(models.Model):
    """ represent aggregation of metrics daily
    """
    metric = models.ForeignKey(Metric)
    user = models.ForeignKey(User)
    user_object_id = models.IntegerField(default=0)

    count = models.IntegerField(default=0)
    unique_count = models.IntegerField(default=0)
    date_up = models.DateField(default=datetime.date.today)
