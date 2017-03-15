# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from collective.behavior.relationleadimage import _
from plone.app.contenttypes.interfaces import IImage
from plone.app.vocabularies.catalog import CatalogSource
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from zope import schema
from zope.interface import Interface
from zope.interface import provider
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ICollectiveBehaviorRelationleadimageLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IRelationLeadImageMarker(Interface):
    """Marker interface for type accepting RelationLeadImage"""


@provider(IFormFieldProvider)
class IRelationLeadImage(model.Schema):

    image_relation = RelationChoice(
        title=_(u'label_relation_leadimage', default=u'Lead Image'),
        description=_(u'description_relation_leadimage',
                      default=u'Please select an image'),
        default=None,
        source=CatalogSource(object_provides=IImage.__identifier__),
        required=False,
    )

    image_caption = schema.TextLine(
        title=_(u'label_leadimage_caption', default=u'Lead Image Caption'),
        description=u'',
        required=False,
    )
