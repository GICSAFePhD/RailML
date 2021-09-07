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
	def CanBeControlledBy(self, aCanBeControlledBy : EntityILref):	# TODO *aCanBeControlledBy
		self.___canBeControlledBy = aCanBeControlledBy
	@ControlledElement.setter
	def ControlledElement(self, aControlledElement : EntityILref):	# TODO *aControlledElement
		self.___controlledElement = aControlledElement

	def create_CanBeControlledBy(self):
		if self.CanBeControlledBy == None:
			self.CanBeControlledBy = []
		self.CanBeControlledBy.append(EntityILref.EntityILref())
	def create_ControlledElement(self):
		if self.ControlledElement == None:
			self.ControlledElement = []
		self.ControlledElement.append(EntityILref.EntityILref())

	def __init__(self):
		super().__init__()
		self.___canBeControlledBy : EntityILref = None
		"""reference to any controller, which can control this permission zone"""
		self.___controlledElement : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 1..*
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 1..*
		# """References to elements which belong to this zone and have the same operating permission"""