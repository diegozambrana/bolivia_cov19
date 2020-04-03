from datetime import datetime
import logging

import django_rq
from django_rq.management.commands import rqscheduler

from registers.jobs import read_data_from_cov19
from django.conf import settings

scheduler = django_rq.get_scheduler()
log = logging.getLogger(__name__)


def clear_scheduled_jobs():
    """
    Delete any existing jobs in the scheduler when the app starts up
    """

    for job in scheduler.get_jobs():
        log.debug("Deleting scheduled job %s", job)
        job.delete()


def register_scheduled_jobs():
    """
    registering jobs to the Scheduler
    """

    # set the start date to 00:30:00AM and the interval 6 hours
    start_date = datetime.today()
    start_date = start_date.replace(hour=0, minute=30, second=0)
    scheduler.schedule(scheduled_time=start_date,
                       func=read_data_from_cov19,
                       interval=settings.TIME_INTERVAL_HOUR * 6)


class Command(rqscheduler.Command):
    def handle(self, *args, **kwargs):
        clear_scheduled_jobs()
        register_scheduled_jobs()
        super(Command, self).handle(*args, **kwargs)
