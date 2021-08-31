#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef, tElementWithIDref
from RailML.Infrastructure import tCrossingConstructionTypeExt, Length, XCrossing, aVerbalConstraint
from typing import List

class UnderCrossing(XCrossing.XCrossing):
	"""An under crossing describes a crossing, where something crosses under the railway line. The most common constructional type of an under crossing is a bridge."""
	@property
	def ConstructionType(self) -> tCrossingConstructionTypeExt:
		return self.___constructionType
	@property
	def BelongsToParent(self) -> tRef:
		return self.___belongsToParent	
	@property
	def AllowedLoadingGauge(self) -> tElementWithIDref:
		return self.___allowedWeightLimit
	@property
	def Length(self) -> Length:
		return self.___length
	@property
	def VerbalConstraint(self) -> aVerbalConstraint:
		return self.___VerbalConstraint

	@ConstructionType.setter
	def ConstructionType(self, aConstructionType : tCrossingConstructionTypeExt):
		self.___constructionType = aConstructionType
	@BelongsToParent.setter
	def BelongsToParent(self, aBelongsToParent : tRef):
		self.___belongsToParent = aBelongsToParent
	@AllowedLoadingGauge.setter
	def AllowedLoadingGauge(self, aAllowedLoadingGauge : tElementWithIDref): #TODO *aAllowedLoadingGauge
		self.___allowedWeightLimit = aAllowedLoadingGauge
	@Length.setter
	def Length(self, *aLength : Length):
		self.___length = aLength
	@VerbalConstraint.setter
	def VerbalConstraint(self, aaVerbalConstraint : aVerbalConstraint):
		self.___VerbalConstraint = aaVerbalConstraint

	def create_AllowedLoadingGauge(self):
		if self.AllowedLoadingGauge == None:
			self.AllowedLoadingGauge = []
		self.AllowedLoadingGauge.append(tElementWithIDref.tElementWithIDref())
	def create_Length(self):
		if self.Length == None:
			self.Length = []
		self.Length.append(Length.Length())
	
	def __init__(self):
		super().__init__()
		self.___constructionType : tCrossingConstructionTypeExt = None
		# @AssociationType Infrastructure.tCrossingConstructionTypeExt
		# """construction type of under crossing: bridge or tunnel"""
		self.___belongsToParent : tRef = None
		# @AssociationType Common.tRef
		# """reference to a parent under crossing"""
		self.___allowedWeightLimit : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to weight limit classes that are allowed to pass over this under crossing"""
		self.___length : Length = None
		# @AssociationType Infrastructure.Length*
		# @AssociationMultiplicity 0..*
		# """length of the under crossing relative to the railway in metres"""
		self.___VerbalConstraint : aVerbalConstraint = None