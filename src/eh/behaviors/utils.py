# -*- coding: utf-8 -*-

from OFS.interfaces import IOrderedContainer
from plone import api
from plone.i18n.normalizer.interfaces import INormalizer
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

import logging
import re


# from eh.behaviors import _


logger = logging.getLogger('eh.behaviors:utils')


def getSettingValue(record, prefix=None):
    """
    :param record: une clé du registre de configuration
    :type record: str
    :return: la valeur enregistrée par le control panel
    """
    if not prefix:
        prefix = 'eh.behaviors.interfaces.IEhBehaviorsSettings.'
    prefix += record
    try:
        reg = api.portal.get_registry_record(prefix)
        return reg
    except Exception:
        logger.info('Cannot get Registry record:' + record)
        return u''


def altLangOneLabel():
    return getSettingValue('default_alt_text_one_label')


def altLangTwoLabel():
    return getSettingValue('default_alt_text_two_label')


checkEmail = re.compile(
    r'[a-zA-Z0-9._%-]+@([a-zA-Z0-9-]+\.)*[a-zA-Z]{2,4}').match


def make_terms(terms, termsList):
    normalizer = getUtility(INormalizer)
    for term in termsList:
        norm = normalizer.normalize(term)
        terms.append(SimpleTerm(value=norm, token=norm, title=term))
    return terms


def make_voc(terms, linesstr):
    return SimpleVocabulary(make_terms(terms, linesstr))


def make_voc_with_blank(terms, linesstr):
    terms.append(SimpleTerm(None, '', u''))
    # import pdb;pdb.set_trace()
    return SimpleVocabulary(make_terms(terms, linesstr))


def getTitleFromVoc(vocabulary, value):
    """
    Utilitaire qui permet d'obtenir le
    libellé (``title``) d'une valeur d'un vocabulaire. Essentiellement destiné
    aux affichages dans les templates.

    :param vocabulary: nom du vocabulaire tel qu'il est défini en tant \
    qu'utilitaire
    :type vocabulary: string
    :param value: valeur pour laquelle on recherche un libellé (``title``)
    :type value: string
    :returns: une chaîne de caractères qui est le ``title`` correspondant à la
        valeur passée en paramètre pour le vocabulaire donné. Si la valeur
        n'existe pas dans le vocabulaire, retourne la valeur elle-même
        passée en paramètre.
    """
    portal = api.portal.get()
    factory = getUtility(IVocabularyFactory, vocabulary)
    types_voc = factory(portal)
    try:
        term = types_voc.getTerm(value).title
    except Exception:
        term = value
    return term


# from http://docs.plone.org/develop/plone/content/listing.html
def get_position_in_parent(obj):
    parent = obj.aq_inner.aq_parent
    ordered = IOrderedContainer(parent, None)
    if ordered is not None:
        return ordered.getObjectPosition(obj.getId())
    return 0


def sort_by_position(a, b):
    """
    Usage :
    sortedMyList = sorted(myList, sort_by_position)
    """
    return get_position_in_parent(a) - get_position_in_parent(b)


def isPublished(obj):
    return api.content.get_state(obj.getObject()) == 'published'


def canView(obj):
    if api.content.get_state(obj) == 'published':
        return True
    if not api.user.is_anonymous():
        current = api.user.get_current()
        username = current.getUserName()
        perm = api.user.get_permissions(
                    username=username, obj=obj
                    )
        return perm['View']
    else:
        return False


def getObjThumbnailSrc(context):
    src = context.absolute_url()
    try:
        thumb = context.thumbnail
        if thumb:
            logger.info(thumb.filename)
            src += '/@@download/thumbnail/' + thumb.filename
            return src
    except Exception:
        pass
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
