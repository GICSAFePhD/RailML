#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import anyAttribute
from RailML.Interlocking import GenericAspect, GenericResetStrategy, GenericRouteType, LevelCrossingTypeList, ElementGroupingTypes, DetectorTypes

from typing import List

class GenericTypes(object):
	"""The list of all possible types being specific for this IM."""
	@property
	def HasAspect(self) -> GenericAspect:
		return self.___hasAspect
	@property
	def HasTVDresetStrategy(self) -> GenericResetStrategy:
		return self.___hasTVDresetStrategy
	@property
	def HasRouteType(self) -> GenericRouteType:
		return self.___hasRouteType
	@property
	def HasLevelCrossingType(self) -> LevelCrossingTypeList:
		return self.___hasLevelCrossingType
	@property
	def HasElementGroupType(self) -> ElementGroupingTypes:
		return self.___hasElementGroupType
	@property
	def HasDetectorTypes(self) -> DetectorTypes:
		return self.___hasDetectorTypes
	@property
	def anyAttribute(self) -> anyAttribute:
		return self.___rail3_anyAttribute

	@HasAspect.setter
	def HasAspect(self, aHasAspect : GenericAspect):	# TODO *aHasAspect
		self.___hasAspect = aHasAspect
	@HasTVDresetStrategy.setter
	def HasTVDresetStrategy(self, aHasTVDresetStrategy : GenericResetStrategy):	# TODO *aHasTVDresetStrategy
		self.___hasTVDresetStrategy = aHasTVDresetStrategy
	@HasRouteType.setter
	def HasRouteType(self, aHasRouteType : GenericRouteType):	# TODO *aHasRouteType
		self.___hasRouteType = aHasRouteType
	@HasLevelCrossingType.setter
	def HasLevelCrossingType(self, aHasLevelCrossingType : LevelCrossingTypeList):	# TODO *aHasLevelCrossingType
		self.___hasLevelCrossingType = aHasLevelCrossingType
	@HasElementGroupType.setter
	def HasElementGroupType(self, aHasElementGroupType : ElementGroupingTypes):	# TODO *aHasElementGroupType
		self.___hasElementGroupType = aHasElementGroupType
	@HasDetectorTypes.setter
	def HasDetectorTypes(self, aHasDetectorTypes : DetectorTypes):	# TODO *aHasDetectorTypes
		self.___hasDetectorTypes = aHasDetectorTypes
	@anyAttribute.setter
	def anyAttribute(self, aanyAttribute : anyAttribute):
		self.___rail3_anyAttribute = aanyAttribute

	def create_HasAspect(self):
		if self.HasAspect == None:
			self.HasAspect = []
		self.HasAspect.append(GenericAspect.GenericAspect())
	def create_HasTVDresetStrategy(self):
		if self.HasTVDresetStrategy == None:
			self.HasTVDresetStrategy = []
		self.HasTVDresetStrategy.append(GenericResetStrategy.GenericResetStrategy())
	def create_HasRouteType(self):
		if self.HasRouteType == None:
			self.HasRouteType = []
		self.HasRouteType.append(GenericRouteType.GenericRouteType())
	def create_HasLevelCrossingType(self):
		if self.HasLevelCrossingType == None:
			self.HasLevelCrossingType = []
		self.HasLevelCrossingType.append(LevelCrossingTypeList.LevelCrossingTypeList())
	def create_HasElementGroupType(self):
		if self.HasElementGroupType == None:
			self.HasElementGroupType = []
		self.HasElementGroupType.append(ElementGroupingTypes.ElementGroupingTypes())
	def create_HasDetectorTypes(self):
		if self.HasDetectorTypes == None:
			self.HasDetectorTypes = []
		self.HasDetectorTypes.append(DetectorTypes.DetectorTypes())

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