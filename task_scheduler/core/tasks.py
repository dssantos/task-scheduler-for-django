
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import random
import time
from task_scheduler.core.models import Numero

@shared_task
def randint(start, stop):
    time.sleep(10)
    numero = random.randint(start, stop)
    n = Numero(numero=numero)
    n.save()
    return numero

