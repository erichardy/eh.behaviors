# -*- coding: utf-8 -*-

"""
cf plone.app.contenttypes.behaviors.richtext.py
"""
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider
from eh.behaviors import _


@provider(IFormFieldProvider)
class IMiscAttributes(model.Schema):
    """Add miscellaneous attributes to objects to be used in views.
    Those attributes are useful only if the specific object view uses them.
    """
    model.fieldset('misc_attributes',
                   label=_(u'Misc attributes'),
                   fields=['position_in_view',
                           'display_title',
                           'display_description',
                           ],)
    position_in_view = schema.Int(
        title=_(u'position wanted in the view, only if used in mixed view'),
        description=_(u'0 = top, 1000 = bottom'),
        min=0,
        max=1000,
        default=0)
    display_title = schema.Bool(
        title=_(u'display the title in the view'),
        description=_(u'unselect to disable'),
        default=True
        )
    display_description = schema.Bool(
        title=_(u'display the description in the view'),
        description=_(u'unselect to disable'),
        default=True
        )


@implementer(IMiscAttributes)
@adapter(IDexterityContent)
class miscAttributes(object):

    def __init__(self, context):
        self.context = context
