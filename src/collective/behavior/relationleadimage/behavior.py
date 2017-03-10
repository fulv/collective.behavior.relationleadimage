# -*- coding: utf-8 -*-
from collective.behavior.relationleadimage.interfaces import IRelationLeadImage
from plone.dexterity.interfaces import IDexterityContent
from plone.namedfile.interfaces import IImageScaleTraversable
from zope.component import adapter
from zope.interface import implementer


@implementer(IRelationLeadImage, IImageScaleTraversable)
@adapter(IDexterityContent)
class RelationLeadImage(object):

    def __init__(self, context):
        self.context = context

    @property
    def image(self):
        if self.context.image_relation.isBroken():
            return None

        image = getattr(self.context.image_relation, 'to_object', None)

        if image:
            return image.image
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
