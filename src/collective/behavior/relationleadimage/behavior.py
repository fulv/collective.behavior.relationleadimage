# -*- coding: utf-8 -*-
from Acquisition import Explicit
from collective.behavior.relationleadimage.interfaces import IRelationLeadImage
from collective.behavior.relationleadimage.interfaces import IRelationLeadImageMarker
from plone.app.contenttypes.behaviors.leadimage import ILeadImage
from plone.app.contenttypes.interfaces import INewsItem
from plone.app.contenttypes.behaviors.leadimage import LeadImage as LeadImageBase
from plone.dexterity.interfaces import IDexterityContent
from plone.namedfile.interfaces import IImageScaleTraversable
from zope.annotation import IAnnotations
from zope.component import adapter
from zope.interface import implementer


#@implementer(IRelationLeadImage, IImageScaleTraversable, IAnnotations)
#@adapter(IDexterityContent)
#class RelationLeadImage(Explicit):
#
#    def __init__(self, context):
#        self.context = context
#
#    @property
#    def image(self):
##        import pdb;pdb.set_trace()
#        return getattr(self.context, 'image', None)
#        relation = self.context.image_relation
#        if not relation or relation.isBroken():
#            image = getattr(self.context, 'image', None)
#            if image:
#                return self.context
#            return None
#
#        image = getattr(self.context.image_relation, 'to_object', None)
#
#        if image:
#            return image
#        return None
#
#    @image.setter
#    def image(self, value):
##        import pdb;pdb.set_trace()
#        setattr(self.context, 'image', value)
#
#    @property
#    def image_relation(self):
#        return getattr(self.context, 'image_relation', None)
#
#    @image_relation.setter
#    def image_relation(self, value):
#        self.context.image_relation = value
#
#    @property
#    def image_caption(self):
#        return getattr(self.context, 'image_caption', '')
#
#    @image_caption.setter
#    def image_caption(self, value):
#        self.context.image_caption = value
#
#
#def relationLeadImage_factory(context):
#    _adapter = RelationLeadImage(context)
##    import pdb;pdb.set_trace()
#    return _adapter.__of__(context)
#

@adapter(IRelationLeadImageMarker)
class LeadImage(LeadImageBase):
    def __init__(self, context):
        import pdb;pdb.set_trace()
        self.context = context
