# -*- coding: utf-8 -*-
from collective.behavior.relationleadimage.interfaces import IRelationLeadImage
from plone.app.contenttypes.behaviors.leadimage import ILeadImage
from plone.app.layout.viewlets import ViewletBase


class LeadImageViewlet(ViewletBase):
    """ A simple viewlet which renders leadimage """

    def update(self):
        context = ILeadImage(self.context)
        image = getattr(context, 'image', None)
        import pdb;pdb.set_trace()

        self.available = True if image else False
        if image:
            self.context = context
