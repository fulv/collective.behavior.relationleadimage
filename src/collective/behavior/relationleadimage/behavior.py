# -*- coding: utf-8 -*-
from Acquisition import Explicit
from collective.behavior.relationleadimage.interfaces import IRelationLeadImage
from plone.app.contenttypes.behaviors.leadimage import ILeadImage
from plone.namedfile.interfaces import IImageScaleTraversable
from zope.annotation import IAnnotations
from zope.interface import adapter
from zope.interface import implementer


@implementer(IRelationLeadImage, IImageScaleTraversable, IAnnotations)
class RelationLeadImage(Explicit):

    def __init__(self, context):
        self.context = context

    @property
    def image(self):
        if self.context.image_relation.isBroken():
            return None

        image = getattr(self.context.image_relation, 'to_object', None)

        if image:
            return image
        return None

    @property
    def image_relation(self):
        return getattr(self.context, 'image_relation', None)

    @image_relation.setter
    def image_relation(self, value):
        self.context.image_relation = value

    @property
    def image_caption(self):
        return getattr(self.context, 'image_caption', '')

    @image_caption.setter
    def image_caption(self, value):
        self.context.image_caption = value


def relationLeadImage_factory(context):
    _adapter = RelationLeadImage(context)
    return _adapter.__of__(context)
