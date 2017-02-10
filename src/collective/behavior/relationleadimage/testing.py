# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.behavior.relationleadimage


class CollectiveBehaviorRelationleadimageLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.behavior.relationleadimage)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.behavior.relationleadimage:default')


COLLECTIVE_BEHAVIOR_RELATIONLEADIMAGE_FIXTURE = CollectiveBehaviorRelationleadimageLayer()


COLLECTIVE_BEHAVIOR_RELATIONLEADIMAGE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_BEHAVIOR_RELATIONLEADIMAGE_FIXTURE,),
    name='CollectiveBehaviorRelationleadimageLayer:IntegrationTesting'
)


COLLECTIVE_BEHAVIOR_RELATIONLEADIMAGE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_BEHAVIOR_RELATIONLEADIMAGE_FIXTURE,),
    name='CollectiveBehaviorRelationleadimageLayer:FunctionalTesting'
)


COLLECTIVE_BEHAVIOR_RELATIONLEADIMAGE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_BEHAVIOR_RELATIONLEADIMAGE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveBehaviorRelationleadimageLayer:AcceptanceTesting'
)
