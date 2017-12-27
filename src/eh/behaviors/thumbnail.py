# -*- coding: utf-8 -*-

from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.namedfile import field as namedfile
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider
from zope.schema.interfaces import IContextAwareDefaultFactory
from zope.schema import Int
from zope.schema import Bool

from eh.behaviors.utils import getSettingValue
from eh.behaviors import _


@provider(IContextAwareDefaultFactory)
def getDefaultWidth(context):
    return getSettingValue('thumb_width')


@provider(IContextAwareDefaultFactory)
def getDefaultHeight(context):
    return getSettingValue('thumb_height')


@provider(IFormFieldProvider)
class IThumbnail(model.Schema):

    model.fieldset('thumbnail',
                   label=_(u'thumbnail'),
                   fields=['thumbnail',
                           'use_thumb_default',
                           'use_thumb_default_sizes',
                           'thumb_width',
                           'thumb_height',
                           ]
                   )
    thumbnail = namedfile.NamedBlobImage(
        title=_(u'label_thumbnail'),
        description=u'',
        required=False,
    )
    use_thumb_default = Bool(
        title=_(u'use default site thumbnail'),
        description=_(u'even if a thumbnail is loaded here'),
        default=False)
    use_thumb_default_sizes = Bool(
        title=_(u'use default site thumbnail size'),
        description=_(u'even if sizes are given here'),
        default=False)
    thumb_width = Int(
        title=_(u'default width'),
        description=_(u'must be integer'),
        defaultFactory=getDefaultWidth,
        required=False
        )
    thumb_height = Int(
        title=_(u'default height'),
        description=_(u'must be integer'),
        defaultFactory=getDefaultHeight,
        required=False
        )


@implementer(IThumbnail)
@adapter(IDexterityContent)
class Thumbnail(object):

    def __init__(self, context):
        self.context = context
