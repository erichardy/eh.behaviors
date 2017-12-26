# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.supermodel import model
from zope.schema import Bool
from zope.schema import TextLine
from eh.behaviors import _


class IEhBehaviorsLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IEhBehaviorsSettings(model.Schema):
    default_alt_text_one_label = TextLine(
        title=_(u'default_alt_text_one_label'),
        default=u'English',
        )
    default_alt_text_two_label = TextLine(
        title=_(u'default_alt_text_two_label'),
        default=u'Spanish',
        )
