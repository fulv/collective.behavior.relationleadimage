# -*- coding: utf-8 -*-
from collective.behavior.relationleadimage.interfaces import IRelationLeadImage
from plone.app.layout.viewlets import ViewletBase


class LeadImageViewlet(ViewletBase):
    """ A simple viewlet which renders leadimage """

    def update(self):
        image = IRelationLeadImage(self.context).image

        self.available = True if image else False
        self.context = image
