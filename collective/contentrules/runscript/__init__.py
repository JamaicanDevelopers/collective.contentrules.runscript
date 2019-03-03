# -*- coding=utf-8 -*-
from zope.i18nmessageid import MessageFactory
import logging


runscriptMessageFactory = MessageFactory('collective.contentrules.runscript')
logger = logging.getLogger('collective.contentrules.runscript')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
