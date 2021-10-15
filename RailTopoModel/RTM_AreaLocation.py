#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.RailTopoModel import RTM_AssociatedNetElement, RTM_EntityLocation
from typing import List

class RTM_AreaLocation(RTM_EntityLocation.RTM_EntityLocation):
	@property
	def AssociatedNetElement(self) -> RTM_AssociatedNetElement:
		return self.___associatedNetElement

	@AssociatedNetElement.setter
	def AssociatedNetElement(self, aAssociatedNetElement : RTM_AssociatedNetElement):
		self.___associatedNetElement = aAssociatedNetElement
    
	def create_AssociatedNetElement(self):
		if self.AssociatedNetElement == None:
			self.AssociatedNetElement = []
		self.AssociatedNetElement.append(RTM_AssociatedNetElement.RTM_AssociatedNetElement())

	def __init__(self):
		super().__init__()
		self.___associatedNetElement : RTM_AssociatedNetElement = None
		# @AssociationType Infrastructure.RTM.RTM_AssociatedNetElement*
		# @AssociationMultiplicity 1..*