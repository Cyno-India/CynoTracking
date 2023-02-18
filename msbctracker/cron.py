
from asyncio.log import logger
from dataclasses import dataclass
import logging
from .views import create, update
import datetime
from . models import *
# datetime object containing current date and time

logger = logging.getLogger(__name__)

def createfunc():
    d  = datetime.datetime.now() 
    te = create()
    logger.info(d)
    logger.info('Created')
    logger.info(te)

def updatefunc():
    d  = datetime.datetime.now() 
    p = Tracker.objects.all().order_by("-Date")[:4]
    print(p)
    # te = update()
    # logger.info(d)
    # logger.info('Update')
    logger.info('UPDAYTTED')


#apart from notfound and expired is bad

