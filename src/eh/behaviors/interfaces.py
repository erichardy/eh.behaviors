# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.supermodel import model
from zope.schema import TextLine
from zope.schema import Int
from eh.behaviors import _


class IEhBehaviorsLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IEhBehaviorsSettings(model.Schema):

    model.fieldset('alt_texts',
                   label=_(u'alt texts'),
                   fields=['default_alt_text_one_label',
                           'default_alt_text_two_label',
                           ]
                   )
    default_alt_text_one_label = TextLine(
        title=_(u'default_alt_text_one_label'),
        default=u'English',
        )
    default_alt_text_two_label = TextLine(
        title=_(u'default_alt_text_two_label'),
        default=u'Spanish',
        )
    model.fieldset('thumbnails',
                   label=_(u'thumbnails'),
                   fields=['default_thumb',
                           'thumb_width',
                           'thumb_height',
                           ]
                   )
    default_thumb = TextLine(
        title=_(u'Name of the default thumb image'),
        description=_(u'in portal_skins/custom/images'),
        default=u'default_thumbnail.jpg',
        )
    thumb_width = Int(
        title=_(u'default width'),
        description=_(u'must be integer'),
        default=70
        )
    thumb_height = Int(
        title=_(u'default height'),
        description=_(u'must be integer'),
        default=70
        )
