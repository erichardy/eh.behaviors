# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import eh.behaviors


class EhBehaviorsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=eh.behaviors)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'eh.behaviors:default')


EH_BEHAVIORS_FIXTURE = EhBehaviorsLayer()


EH_BEHAVIORS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EH_BEHAVIORS_FIXTURE,),
    name='EhBehaviorsLayer:IntegrationTesting'
)


EH_BEHAVIORS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EH_BEHAVIORS_FIXTURE,),
    name='EhBehaviorsLayer:FunctionalTesting'
)


EH_BEHAVIORS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EH_BEHAVIORS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='EhBehaviorsLayer:AcceptanceTesting'
)
