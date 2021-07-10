#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import tElementProjectionSymbolOrientationExt
from Infrastructure import ProjectionCoordinate
from Infrastructure import VisualizationBaseElement
from typing import List

class ElementProjectionSymbol(VisualizationBaseElement):
	def setExternalIconRef(self, aExternalIconRef : str):
		self.___externalIconRef = aExternalIconRef

	def getExternalIconRef(self) -> str:
		return self.___externalIconRef

	def setOrientation(self, aOrientation : tElementProjectionSymbolOrientationExt):
		self.___orientation = aOrientation

	def getOrientation(self) -> tElementProjectionSymbolOrientationExt:
		return self.___orientation

	def setIsLocatedAt(self, aIsLocatedAt : ProjectionCoordinate):
		self._isLocatedAt = aIsLocatedAt

	def getIsLocatedAt(self) -> ProjectionCoordinate:
		return self._isLocatedAt

	def __init__(self):
		self.___externalIconRef : str = None
		"""reference to an external Icon or symbol"""
		self.___orientation : tElementProjectionSymbolOrientationExt = None
		# @AssociationType Infrastructure.tElementProjectionSymbolOrientationExt
		# """orientation of the external icon or symbol with respect to its standard orientation (up)"""
		self._isLocatedAt : ProjectionCoordinate = None
		# @AssociationType Infrastructure.ProjectionCoordinate
		# @AssociationMultiplicity 1
		# """coordinate, where the icon or symbol shall be placed with its reference point"""

