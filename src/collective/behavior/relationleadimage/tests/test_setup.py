# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from collective.behavior.relationleadimage.testing import COLLECTIVE_BEHAVIOR_RELATIONLEADIMAGE_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.behavior.relationleadimage is properly installed."""

    layer = COLLECTIVE_BEHAVIOR_RELATIONLEADIMAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.behavior.relationleadimage is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.behavior.relationleadimage'))

    def test_browserlayer(self):
        """Test that ICollectiveBehaviorRelationleadimageLayer is registered."""
        from collective.behavior.relationleadimage.interfaces import (
            ICollectiveBehaviorRelationleadimageLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectiveBehaviorRelationleadimageLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_BEHAVIOR_RELATIONLEADIMAGE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.behavior.relationleadimage'])

    def test_product_uninstalled(self):
        """Test if collective.behavior.relationleadimage is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.behavior.relationleadimage'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveBehaviorRelationleadimageLayer is removed."""
        from collective.behavior.relationleadimage.interfaces import \
            ICollectiveBehaviorRelationleadimageLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveBehaviorRelationleadimageLayer, utils.registered_layers())
