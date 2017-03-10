# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.behavior.relationleadimage.testing import COLLECTIVE_BEHAVIOR_RELATIONLEADIMAGE_INTEGRATION_TESTING  # noqa
from plone import api

import unittest

cbrli = 'collective.behavior.relationleadimage'


class TestSetup(unittest.TestCase):
    """Test that collective.behavior.relationleadimage is properly installed.
    """

    layer = COLLECTIVE_BEHAVIOR_RELATIONLEADIMAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.behavior.relationleadimage is installed."""
        self.assertTrue(self.installer.isProductInstalled(cbrli))

    def test_browserlayer(self):
        """Test that ICollectiveBehaviorRelationleadimageLayer is registered.
        """
        from collective.behavior.relationleadimage.interfaces import (
            ICollectiveBehaviorRelationleadimageLayer as ICBRLIL)
        from plone.browserlayer import utils
        self.assertIn(ICBRLIL, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_BEHAVIOR_RELATIONLEADIMAGE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts([cbrli])

    def test_product_uninstalled(self):
        """Test if collective.behavior.relationleadimage is cleanly
           uninstalled.
        """
        self.assertFalse(self.installer.isProductInstalled(cbrli))

    def test_browserlayer_removed(self):
        """Test that ICollectiveBehaviorRelationleadimageLayer is removed."""
        from collective.behavior.relationleadimage.interfaces import \
            ICollectiveBehaviorRelationleadimageLayer as ICBRLIL
        from plone.browserlayer import utils
        self.assertNotIn(ICBRLIL, utils.registered_layers())
