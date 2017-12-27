# -*- coding: utf-8 -*-

from plone import api
import logging

from eh.behaviors.utils import getSettingValue
from eh.behaviors.thumbnail import IThumbnail

# from eh.behaviors import _


logger = logging.getLogger('eh.behaviors:utils_thumbnails')


def thumbnailProvided(obj):
    """
    :param obj: the object for which we look for a thumbnail
    :type obj: any zope/plone object
    :returns: ``True`` if the thumbnail behavior is activated
        for this ``obj``. If the attr ``use_thumb_default``
        is True or if a thumbnail is present, returns ``True``.
        Returns ``False`` if the behavior is not activated or
        if no filename.
    .. note:: even if the behavior is not activated, it is possible
        to get a thumbnail if a leadImage is present of getting
        default site thumbnail... So, if this function returns ``False``,
        the function ``getDefaultThumbSRC`` is still avaliable.
    """
    provided = IThumbnail.providedBy(obj)
    if not provided:
        return False
    if obj.use_thumb_default:
        return True
    try:
        return obj.thumbnail.filename != u''
    except Exception:
        return False


def getThumbSRC(obj, leadImage=False):
    if not thumbnailProvided(obj):
        return getObjThumbnailSrc(
            context=None,
            leadImage=leadImage
            )
    if obj.use_thumb_default:
        return getObjThumbnailSrc(
            context=None,
            leadImage=leadImage
            )
    else:
        return getObjThumbnailSrc(
            context=obj,
            leadImage=leadImage
            )


def getDefaultThumbSRC():
    """
    :returns: the default site thumbnail SRC URL
    """
    return getObjThumbnailSrc(
            context=None,
            leadImage=False
            )


def getObjThumbnailSrc(context=None, leadImage=False):
    """
    :param context: the object for which we get the thumbnail URL. If not
        context, context is ``portal``
    :type context: any zope/plone object
    :param leadImage: if no thumbnail but a lead image, takes it
    :type leadImage: boolean
    :returns: the URL of the object thumbnail or, if not context, the default
        site thumbnail. But, if ``leadImage`` is ``True``, tries to returns
        the Image field URL instead.
    """
    if not context:
        context = api.portal.get()
    src = context.absolute_url()
    try:
        thumb = context.thumbnail
        if thumb:
            src += '/@@download/thumbnail/' + thumb.filename
            return src
    except Exception:
        pass
    if leadImage:
        try:
            image = context.image
            if image:
                src += '/@@download/image/' + image.filename
                return src
        except Exception:
            pass
    default = getSettingValue('default_thumb')
    portal = api.portal.get()
    return portal.absolute_url() + '/images/' + default
