#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tRef
from Infrastructure import SpotProjection
from Infrastructure import LinearProjection
from Infrastructure import AreaProjection
from Infrastructure import VisualizationBaseElement
from typing import List

class Visualization(VisualizationBaseElement):
	def setPositioningSystemRef(self, aPositioningSystemRef : tRef):
		self.___positioningSystemRef = aPositioningSystemRef

	def getPositioningSystemRef(self) -> tRef:
		return self.___positioningSystemRef

	def setSpotElementProjection(self, *aSpotElementProjection : SpotProjection*):
		self._spotElementProjection = aSpotElementProjection

	def getSpotElementProjection(self) -> SpotProjection*:
		return self._spotElementProjection

	def setLinearElementProjection(self, *aLinearElementProjection : LinearProjection*):
		self._linearElementProjection = aLinearElementProjection

	def getLinearElementProjection(self) -> LinearProjection*:
		return self._linearElementProjection

	def setAreaElementProjection(self, *aAreaElementProjection : AreaProjection*):
		self._areaElementProjection = aAreaElementProjection

	def getAreaElementProjection(self) -> AreaProjection*:
		return self._areaElementProjection

	def __init__(self):
		self.___positioningSystemRef : tRef = None
		# @AssociationType Common.tRef
		# """reference to a positioning system"""
		self._spotElementProjection : SpotProjection = None
		# @AssociationType Infrastructure.SpotProjection*
		# @AssociationMultiplicity 0..*
		# """element projection as spot location (1 coordinate)"""
		self._linearElementProjection : LinearProjection = None
		# @AssociationType Infrastructure.LinearProjection*
		# @AssociationMultiplicity 0..*
		# """element projection as linear location (min 2 coordinates)"""
		self._areaElementProjection : AreaProjection = None
		# @AssociationType Infrastructure.AreaProjection*
		# @AssociationMultiplicity 0..*
		# """element projection as area location (min 3 coordinates)"""

