
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import random
from task_scheduler.core.models import Numero

@shared_task
def randint(start, stop):
    numero = random.randint(start, stop)
    n = Numero(numero=numero)
    n.save()
    return numero

