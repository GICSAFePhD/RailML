#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import tElementProjectionSymbolOrientationExt
from RailML.Infrastructure import ProjectionCoordinate
from RailML.Infrastructure import VisualizationBaseElement
from typing import List

class ElementProjectionSymbol(VisualizationBaseElement.VisualizationBaseElement):
	@property
	def ExternalIconRef(self) -> str:
		return self.___externalIconRef
	@property
	def Orientation(self) -> tElementProjectionSymbolOrientationExt:
		return self.___orientation
	@property
	def IsLocatedAt(self) -> ProjectionCoordinate:
		return self.___isLocatedAt

	@ExternalIconRef.setter
	def ExternalIconRef(self, aExternalIconRef : str):
		self.___externalIconRef = aExternalIconRef
	@Orientation.setter
	def Orientation(self, aOrientation : tElementProjectionSymbolOrientationExt):
		self.___orientation = aOrientation
	@IsLocatedAt.setter
	def IsLocatedAt(self, aIsLocatedAt : ProjectionCoordinate):
		self.___isLocatedAt = aIsLocatedAt

	def __init__(self):
		super().__init__()
		self.___externalIconRef : str = None
		"""reference to an external Icon or symbol"""
		self.___orientation : tElementProjectionSymbolOrientationExt = None
		# @AssociationType Infrastructure.tElementProjectionSymbolOrientationExt
		# """orientation of the external icon or symbol with respect to its standard orientation (up)"""
		self.___isLocatedAt : ProjectionCoordinate = None
		# @AssociationType Infrastructure.ProjectionCoordinate
		# @AssociationMultiplicity 1
		# """coordinate, where the icon or symbol shall be placed with its reference point"""