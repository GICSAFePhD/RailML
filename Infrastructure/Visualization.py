#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef
from RailML.Infrastructure import SpotProjection, LinearProjection, AreaProjection, VisualizationBaseElement
from typing import List

class Visualization(VisualizationBaseElement.VisualizationBaseElement):
	@property
	def PositioningSystemRef(self) -> tRef:
		return self.___positioningSystemRef
	@property
	def SpotElementProjection(self) -> SpotProjection:
		return self.___spotElementProjection
	@property
	def LinearElementProjection(self) -> LinearProjection:
		return self.___linearElementProjection
	@property
	def AreaElementProjection(self) -> AreaProjection:
		return self.___areaElementProjection

	@PositioningSystemRef.setter
	def PositioningSystemRef(self, aPositioningSystemRef : tRef):
		self.___positioningSystemRef = aPositioningSystemRef
	@SpotElementProjection.setter
	def SpotElementProjection(self, *aSpotElementProjection : SpotProjection):
		self.___spotElementProjection = aSpotElementProjection
	@LinearElementProjection.setter
	def LinearElementProjection(self, *aLinearElementProjection : LinearProjection):
		self.___linearElementProjection = aLinearElementProjection
	@AreaElementProjection.setter
	def AreaElementProjection(self, *aAreaElementProjection : AreaProjection):
		self.___areaElementProjection = aAreaElementProjection

	def __init__(self):
		self.___positioningSystemRef : tRef = tRef.tRef()
		# @AssociationType Common.tRef
		# """reference to a positioning system"""
		self.___spotElementProjection : SpotProjection = SpotProjection.SpotProjection()
		# @AssociationType Infrastructure.SpotProjection*
		# @AssociationMultiplicity 0..*
		# """element projection as spot location (1 coordinate)"""
		self.___linearElementProjection : LinearProjection = LinearProjection.LinearProjection()
		# @AssociationType Infrastructure.LinearProjection*
		# @AssociationMultiplicity 0..*
		# """element projection as linear location (min 2 coordinates)"""
		self.___areaElementProjection : AreaProjection = AreaProjection.AreaProjection()
		# @AssociationType Infrastructure.AreaProjection*
		# @AssociationMultiplicity 0..*
		# """element projection as area location (min 3 coordinates)"""

