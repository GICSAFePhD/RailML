#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.GenericAspect import GenericAspect
from RailML.Interlocking.GenericResetStrategy import GenericResetStrategy
from RailML.Interlocking.GenericRouteType import GenericRouteType
from RailML.Interlocking.LevelCrossingTypeList import LevelCrossingTypeList
from RailML.Interlocking.ElementGroupingTypes import ElementGroupingTypes
from RailML.Interlocking.DetectorTypes import DetectorTypes
from RailML.Common.anyAttribute import anyAttribute
from typing import List

class GenericTypes(object):
	"""The list of all possible types being specific for this IM."""
	def setHasAspect(self, *aHasAspect : GenericAspect):
		self._hasAspect = aHasAspect

	def getHasAspect(self) -> GenericAspect:
		return self._hasAspect

	def setHasTVDresetStrategy(self, *aHasTVDresetStrategy : GenericResetStrategy):
		self._hasTVDresetStrategy = aHasTVDresetStrategy

	def getHasTVDresetStrategy(self) -> GenericResetStrategy:
		return self._hasTVDresetStrategy

	def setHasRouteType(self, *aHasRouteType : GenericRouteType):
		self._hasRouteType = aHasRouteType

	def getHasRouteType(self) -> GenericRouteType:
		return self._hasRouteType

	def setHasLevelCrossingType(self, *aHasLevelCrossingType : LevelCrossingTypeList):
		self._hasLevelCrossingType = aHasLevelCrossingType

	def getHasLevelCrossingType(self) -> LevelCrossingTypeList:
		return self._hasLevelCrossingType

	def setHasElementGroupType(self, *aHasElementGroupType : ElementGroupingTypes):
		self._hasElementGroupType = aHasElementGroupType

	def getHasElementGroupType(self) -> ElementGroupingTypes:
		return self._hasElementGroupType

	def setHasDetectorTypes(self, *aHasDetectorTypes : DetectorTypes):
		self._hasDetectorTypes = aHasDetectorTypes

	def getHasDetectorTypes(self) -> DetectorTypes:
		return self._hasDetectorTypes

	def __init__(self):
		self._hasAspect : GenericAspect = None
		# @AssociationType Interlocking.GenericAspect*
		# @AssociationMultiplicity 2..*
		# """Classification of signal aspects."""
		self._hasTVDresetStrategy : GenericResetStrategy = None
		# @AssociationType Interlocking.GenericResetStrategy*
		# @AssociationMultiplicity 0..*
		# """Classification of TVD section reset strategies"""
		self._hasRouteType : GenericRouteType = None
		# @AssociationType Interlocking.GenericRouteType*
		# @AssociationMultiplicity 1..*
		# """Classification of route types."""
		self._hasLevelCrossingType : LevelCrossingTypeList = None
		# @AssociationType Interlocking.LevelCrossingTypeList*
		# @AssociationMultiplicity 0..*
		# """Classification of basic level crossing types."""
		self._hasElementGroupType : ElementGroupingTypes = None
		# @AssociationType Interlocking.ElementGroupingTypes*
		# @AssociationMultiplicity 0..*
		# """Classification of element groups used for operation from the interlock."""
		self._hasDetectorTypes : DetectorTypes = None
		# @AssociationType Interlocking.DetectorTypes*
		# @AssociationMultiplicity 0..*
		# """The list of detector type classification."""
		self.___rail3_anyAttribute : anyAttribute = None
		"""# @AssociationKind Aggregation"""

