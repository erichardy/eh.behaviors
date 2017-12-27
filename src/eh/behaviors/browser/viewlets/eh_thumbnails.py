# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import common as base
from eh.behaviors.utils import getSettingValue
from eh.behaviors.utils_thumbnails import thumbnailProvided
from eh.behaviors.utils_thumbnails import getThumbSRC

import logging

logger = logging.getLogger('eh_thumbnails')


class ehThumbnail(base.ViewletBase):
    """
    This viewlet is to be used for a specific object view
    """

    def _thumbnailProvided(self):
        return thumbnailProvided(self.context)

    def _getThumbSRC(self, leadImage=False):
        return getThumbSRC(
            self.context,
            leadImage=leadImage
            )

    def getThumbSize(self):
        co = self.context
        size = {}
        size['width'] = u''
        size['height'] = u''
        if co.use_thumb_default_sizes:
            size['width'] = getSettingValue('thumb_width')
            size['height'] = getSettingValue('thumb_height')
            return size
        if co.thumb_width:
            size['width'] = co.thumb_width
        if co.thumb_height:
            size['height'] = co.thumb_height
        return size


class ehThumbnails(base.ViewletBase):
    """
    This viewlet is to display a set of object thumbnails
    TO BE DONE !!
    """
    pass
