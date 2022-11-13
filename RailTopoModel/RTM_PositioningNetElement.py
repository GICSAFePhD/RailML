#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.RailTopoModel import AssociatedPositioningSystem, RTM_CompositionNetElement
from typing import List

class RTM_PositioningNetElement(RTM_CompositionNetElement.RTM_CompositionNetElement):
	@property
	def AssociatedPositioningSystem(self) -> AssociatedPositioningSystem:
		return self.___associatedPositioningSystem
	
	@AssociatedPositioningSystem.setter
	def AssociatedPositioningSystem(self, aAssociatedPositioningSystem : AssociatedPositioningSystem):
		self.___associatedPositioningSystem = aAssociatedPositioningSystem
    
	def create_AssociatedPositioningSystem(self):
		if self.AssociatedPositioningSystem == None:
			self.AssociatedPositioningSystem = []
		self.AssociatedPositioningSystem.append(AssociatedPositioningSystem.AssociatedPositioningSystem())

	def __init__(self):
		super().__init__()
		self.___associatedPositioningSystem : AssociatedPositioningSystem = None
		# @AssociationType Infrastructure.RTM.RTM_AssociatedPositioningSystem*
		# @AssociationMultiplicity 1..*