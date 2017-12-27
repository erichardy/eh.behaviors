# -*- coding: utf-8 -*-

"""
cf plone.app.contenttypes.behaviors.richtext.py
"""
from collective import dexteritytextindexer
from plone.app.textfield import RichText as RichTextField
from plone.app.z3cform.widget import RichTextFieldWidget
from plone.autoform import directives as form
from plone.autoform.interfaces import IFormFieldProvider
from plone.autoform.view import WidgetsView
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from eh.behaviors.utils import getSettingValue
from zope import schema
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider
from zope.schema import TextLine
from zope.schema.interfaces import IContextAwareDefaultFactory
from eh.behaviors import _


@provider(IContextAwareDefaultFactory)
def getLabelOne(context):
    return getSettingValue('default_alt_text_one_label')


@provider(IContextAwareDefaultFactory)
def getLabelTwo(context):
    return getSettingValue('default_alt_text_two_label')


@provider(IFormFieldProvider)
class IAltTexts(model.Schema):
    """Add alternate texts option to content
    """
    model.fieldset('alt_texts',
                   label=_(u'Alternates texts'),
                   fields=['display_one',
                           'label_one',
                           'presentation_one',
                           'display_two',
                           'label_two',
                           'presentation_two',
                           ],)
    display_one = schema.Bool(
        title=_(u'display first Alt text'),
        description=_(u'unselect to disable'),
        default=True
        )
    label_one = TextLine(
        title=_(u'label for alt text one button'),
        defaultFactory=getLabelOne,
        required=False,
        )
    dexteritytextindexer.searchable('presentation_one')
    presentation_one = RichTextField(title=_(u'Alt text one'),
                                     description=_(u'presentation one'),
                                     required=False
                                     )
    form.widget('presentation_one', RichTextFieldWidget)
    model.primary('presentation_one')

    display_two = schema.Bool(
        title=_(u'display second Alt text'),
        description=_(u'unselect to disable'),
        default=False
        )
    label_two = TextLine(
        title=_(u'label for alt text two button'),
        defaultFactory=getLabelTwo,
        required=False,
        )
    dexteritytextindexer.searchable('presentation_two')
    presentation_two = RichTextField(title=_(u'Alt text two'),
                                     description=_(u'presentation two'),
                                     required=False
                                     )
    form.widget('presentation_two', RichTextFieldWidget)
    model.primary('presentation_two')


@implementer(IAltTexts)
@adapter(IDexterityContent)
class altTexts(object):

    def __init__(self, context):
        self.context = context


class WidgetView(WidgetsView):
    schema = IAltTexts
