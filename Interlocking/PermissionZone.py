#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import EntityILref, TrackAsset
from typing import List

class PermissionZone(TrackAsset.TrackAsset):
	"""A restricted area inside a station which can be controlled from a different controller as the rest of the station"""
	@property
	def CanBeControlledBy(self) -> EntityILref:
		return self.___canBeControlledBy
	@property
	def ControlledElement(self) -> EntityILref:
		return self.___controlledElement

	@CanBeControlledBy.setter
	def CanBeControlledBy(self, *aCanBeControlledBy : EntityILref):
		self.___canBeControlledBy = aCanBeControlledBy
	@ControlledElement.setter
	def ControlledElement(self, *aControlledElement : EntityILref):
		self.___controlledElement = aControlledElement

	def __init__(self):
		self.___canBeControlledBy : EntityILref = EntityILref.EntityILref()
		"""reference to any controller, which can control this permission zone"""
		self.___controlledElement : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 1..*
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 1..*
		# """References to elements which belong to this zone and have the same operating permission"""

