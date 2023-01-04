
from asyncio.log import logger
from dataclasses import dataclass
import logging
from .views import create, update
import datetime
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
    te = update()
    logger.info(d)
    logger.info('Update')
    logger.info(te)


#apart from notfound and expired is bad

