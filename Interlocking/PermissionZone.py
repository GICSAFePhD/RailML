#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.TrackAsset import TrackAsset
from typing import List

class PermissionZone(TrackAsset):
	"""A restricted area inside a station which can be controlled from a different controller as the rest of the station"""
	def setCanBeControlledBy(self, *aCanBeControlledBy : EntityILref):
		self._canBeControlledBy = aCanBeControlledBy

	def getCanBeControlledBy(self) -> EntityILref:
		return self._canBeControlledBy

	def setControlledElement(self, *aControlledElement : EntityILref):
		self._controlledElement = aControlledElement

	def getControlledElement(self) -> EntityILref:
		return self._controlledElement

	def __init__(self):
		self._canBeControlledBy : EntityILref = None
		"""reference to any controller, which can control this permission zone"""
		self._controlledElement : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 1..*
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 1..*
		# """References to elements which belong to this zone and have the same operating permission"""

