# -*- coding: utf-8 -*-

from collective import dexteritytextindexer
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from eh.behaviors import _
from zope import schema
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider


@provider(IFormFieldProvider)
class IStartEndDates(model.Schema):
    """Add start and end dates to content
    """

    model.fieldset('dates',
                   fields=['display_dates',
                           'display_time',
                           'start_date',
                           'end_date',
                           ],
                   )
    display_dates = schema.Bool(title=_(u'display start and end dates ?'),
                                description=_(u'unselect to disable'),
                                default=True
                                )
    display_time = schema.Bool(title=_(u'display time with dates ?'),
                               description=_(u'unselect to disable'),
                               default=False
                               )
    dexteritytextindexer.searchable('start_date')
    start_date = schema.Datetime(title=_(u'start date'),
                                 description=_(u''),
                                 required=False,
                                 )
    dexteritytextindexer.searchable('end_date')
    end_date = schema.Datetime(title=_(u'end date'),
                               description=_(u''),
                               required=False,
                               )


@implementer(IStartEndDates)
@adapter(IDexterityContent)
class startEndDates(object):

    def __init__(self, context):
        self.context = context
