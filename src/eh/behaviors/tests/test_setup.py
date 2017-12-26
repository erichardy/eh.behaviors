# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from eh.behaviors.testing import EH_BEHAVIORS_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that eh.behaviors is properly installed."""

    layer = EH_BEHAVIORS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if eh.behaviors is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'eh.behaviors'))

    def test_browserlayer(self):
        """Test that IEhBehaviorsLayer is registered."""
        from eh.behaviors.interfaces import (
            IEhBehaviorsLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IEhBehaviorsLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = EH_BEHAVIORS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['eh.behaviors'])

    def test_product_uninstalled(self):
        """Test if eh.behaviors is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'eh.behaviors'))

    def test_browserlayer_removed(self):
        """Test that IEhBehaviorsLayer is removed."""
        from eh.behaviors.interfaces import \
            IEhBehaviorsLayer
        from plone.browserlayer import utils
        self.assertNotIn(
           IEhBehaviorsLayer,
           utils.registered_layers())
