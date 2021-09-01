#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import anyAttribute
from RailML.Interlocking import GenericAspect, GenericResetStrategy, GenericRouteType, LevelCrossingTypeList, ElementGroupingTypes, DetectorTypes

from typing import List

class GenericTypes(object):
	"""The list of all possible types being specific for this IM."""
	@property
	def GenericAspect(self) -> GenericAspect:
		return self.___hasAspect
	@property
	def GenericResetStrategy(self) -> GenericResetStrategy:
		return self.___hasTVDresetStrategy
	@property
	def GenericRouteType(self) -> GenericRouteType:
		return self.___hasRouteType
	@property
	def LevelCrossingTypeList(self) -> LevelCrossingTypeList:
		return self.___hasLevelCrossingType
	@property
	def ElementGroupingTypes(self) -> ElementGroupingTypes:
		return self.___hasElementGroupType
	@property
	def DetectorTypes(self) -> DetectorTypes:
		return self.___hasDetectorTypes
	@property
	def anyAttribute(self) -> anyAttribute:
		return self.___rail3_anyAttribute

	@GenericAspect.setter
	def GenericAspect(self, *aGenericAspect : GenericAspect):
		self.___hasAspect = aGenericAspect
	@GenericResetStrategy.setter
	def GenericResetStrategy(self, *aGenericResetStrategy : GenericResetStrategy):
		self.___hasTVDresetStrategy = aGenericResetStrategy
	@GenericRouteType.setter
	def GenericRouteType(self, *aGenericRouteType : GenericRouteType):
		self.___hasRouteType = aGenericRouteType
	@LevelCrossingTypeList.setter
	def LevelCrossingTypeList(self, *aLevelCrossingTypeList : LevelCrossingTypeList):
		self.___hasLevelCrossingType = aLevelCrossingTypeList
	@ElementGroupingTypes.setter
	def ElementGroupingTypes(self, *aElementGroupingTypes : ElementGroupingTypes):
		self.___hasElementGroupType = aElementGroupingTypes
	@DetectorTypes.setter
	def DetectorTypes(self, *aDetectorTypes : DetectorTypes):
		self.___hasDetectorTypes = aDetectorTypes
	@anyAttribute.setter
	def anyAttribute(self, aanyAttribute : anyAttribute):
		self.___rail3_anyAttribute = aanyAttribute

	def __init__(self):
		self.___hasAspect : GenericAspect = None
		# @AssociationType Interlocking.GenericAspect*
		# @AssociationMultiplicity 2..*
		# """Classification of signal aspects."""
		self.___hasTVDresetStrategy : GenericResetStrategy = None
		# @AssociationType Interlocking.GenericResetStrategy*
		# @AssociationMultiplicity 0..*
		# """Classification of TVD section reset strategies"""
		self.___hasRouteType : GenericRouteType = None
		# @AssociationType Interlocking.GenericRouteType*
		# @AssociationMultiplicity 1..*
		# """Classification of route types."""
		self.___hasLevelCrossingType : LevelCrossingTypeList = None
		# @AssociationType Interlocking.LevelCrossingTypeList*
		# @AssociationMultiplicity 0..*
		# """Classification of basic level crossing types."""
		self.___hasElementGroupType : ElementGroupingTypes = None
		# @AssociationType Interlocking.ElementGroupingTypes*
		# @AssociationMultiplicity 0..*
		# """Classification of element groups used for operation from the interlock."""
		self.___hasDetectorTypes : DetectorTypes = None
		# @AssociationType Interlocking.DetectorTypes*
		# @AssociationMultiplicity 0..*
		# """The list of detector type classification."""
		self.___rail3_anyAttribute : anyAttribute = None
		"""# @AssociationKind Aggregation"""

