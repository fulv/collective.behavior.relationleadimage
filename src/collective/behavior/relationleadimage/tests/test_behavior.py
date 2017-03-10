# -*- coding: utf-8 -*-
from collective.behavior.relationleadimage.testing import COLLECTIVE_BEHAVIOR_RELATIONLEADIMAGE_FUNCTIONAL_TESTING  # noqa
from plone import api
from plone.app.contenttypes.interfaces import IPloneAppContenttypesLayer
from plone.app.testing import setRoles
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.app.testing import TEST_USER_ID
from plone.dexterity.fti import DexterityFTI
from plone.testing.z2 import Browser
from zope.interface import alsoProvides

import unittest

cbrli = 'collective.behavior.relationleadimage'


class RelationLeadImageBehaviorFunctionalTest(unittest.TestCase):
    """Test the collective.behavior.relationleadimage behavior. """

    layer = COLLECTIVE_BEHAVIOR_RELATIONLEADIMAGE_FUNCTIONAL_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.portal_url = self.portal.absolute_url()
        self.installer = api.portal.get_tool('portal_quickinstaller')
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = DexterityFTI('leadimagefolder')
        self.portal.portal_types._setObject('leadimagefolder', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.behaviors = (
            '{0}.IRelationLeadImage'.format(cbrli),
        )
        self.fti = fti
        alsoProvides(self.portal.REQUEST, IPloneAppContenttypesLayer)
        alsoProvides(self.request, IPloneAppContenttypesLayer)
        from collective.behavior.relationleadimage.interfaces import (
            IRelationLeadImage
        )
        alsoProvides(self.request, IRelationLeadImage)
        api.content.create(
            self.portal,
            'leadimagefolder',
            id='leadimagefolder',
            title=u'Folder with a lead image'
        )
        import transaction
        transaction.commit()
        # Set up browser
        self.browser = Browser(app)
        self.browser.handleErrors = False
        self.browser.addHeader(
            'Authorization',
            'Basic {0}:{1}'.format(SITE_OWNER_NAME, SITE_OWNER_PASSWORD,)
        )

    def test_lead_image_in_edit_form(self):
        self.browser.open(self.portal_url + '/leadimagefolder/edit')
        self.assertTrue('Lead Image Caption' in self.browser.contents)
        self.assertTrue('Lead Image' in self.browser.contents)
