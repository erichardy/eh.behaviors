# -*- coding: utf-8 -*-


from plone.app.layout.viewlets import common as base
from eh.behaviors.thumbnail import IThumbnail

import logging


logger = logging.getLogger('eh_thumbnails')


class ehThumbnails(base.ViewletBase):

    def thumbnailProvided(self):
        provided = IThumbnail.providedBy(self.context)
        try:
            filename = self.context.thumbnail.filename
            return (provided and filename)
        except Exception:
            return False

    def getThumbSRC(self):
        try:
            filename = self.context.thumbnail.filename
        except Exception:
            return False
        url = self.context.absolute_url() + '/@@download/thumbnail/'
        url += filename
        return url
