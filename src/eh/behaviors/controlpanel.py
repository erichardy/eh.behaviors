# -*- coding: utf-8 -*-

from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from eh.behaviors import _
from eh.behaviors.interfaces import IEhBehaviorsSettings


class IEhBehaviorsSettingsForm(RegistryEditForm):
    schema = IEhBehaviorsSettings
    label = _(u'eh.behaviors Settings')
    description = _(u'eh.behaviors Settings Description')

    """
    def updateFields(self):
        super(IIuemAgreementsSettingsForm, self).updateFields()

    def updateWidgets(self):
        super(IIuemAgreementsSettingsForm, self).updateWidgets()
    """


class IEhBehaviorsSettingsControlPanel(ControlPanelFormWrapper):
    form = IEhBehaviorsSettingsForm
