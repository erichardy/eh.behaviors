# -*- coding: utf-8 -*-
from plone.app.contenttypes import _
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.namedfile import field as namedfile
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider


@provider(IFormFieldProvider)
class IThumbnail(model.Schema):

    model.fieldset('thumbnail',
                   label=_(u'thumbnail'),
                   fields=['thumbnail',
                           ]
                   )
    thumbnail = namedfile.NamedBlobImage(
        title=_(u'label_thumbnail', default=u'thumbnail'),
        description=u'',
        required=False,
    )


@implementer(IThumbnail)
@adapter(IDexterityContent)
class Thumbnail(object):

    def __init__(self, context):
        self.context = context
