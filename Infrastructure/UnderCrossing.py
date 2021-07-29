#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef, tElementWithIDref
from RailML.Infrastructure import tCrossingConstructionTypeExt, Length, XCrossing, aVerbalConstraint
from typing import List

class UnderCrossing(XCrossing.XCrossing):
	"""An under crossing describes a crossing, where something crosses under the railway line. The most common constructional type of an under crossing is a bridge."""
	def setAllowedWeightLimit(self, *aAllowedWeightLimit : tElementWithIDref):
		self._allowedWeightLimit = aAllowedWeightLimit
	def setLength(self, *aLength : Length):
		self._length = aLength

	@property
	def ConstructionType(self) -> tCrossingConstructionTypeExt:
		return self.___constructionType
	@property
	def BelongsToParent(self) -> tRef:
		return self.___belongsToParent	
	@property
	def AllowedLoadingGauge(self) -> tElementWithIDref:
		return self.___allowedLoadingGauge
	@property
	def Length(self) -> Length:
		return self.___length
	@property
	def GradientCurve(self) -> aVerbalConstraint:
		return self.___unnamed_aVerbalConstraint_

	@ConstructionType.setter
	def ConstructionType(self, aConstructionType : tCrossingConstructionTypeExt):
		self.___constructionType = aConstructionType
	@BelongsToParent.setter
	def BelongsToParent(self, aBelongsToParent : tRef):
		self.___belongsToParent = aBelongsToParent
	@AllowedLoadingGauge.setter
	def AllowedLoadingGauge(self, *aAllowedLoadingGauge : tElementWithIDref):
		self.___allowedLoadingGauge = aAllowedLoadingGauge
	@Length.setter
	def Length(self, *aLength : Length):
		self.___length = aLength
	@GradientCurve.setter
	def VerbalConstraint(self, aaVerbalConstraint : aVerbalConstraint):
		self.___unnamed_aVerbalConstraint_ = aaVerbalConstraint

	def __init__(self):
		self.___constructionType : tCrossingConstructionTypeExt = tCrossingConstructionTypeExt.tCrossingConstructionTypeExt()
		# @AssociationType Infrastructure.tCrossingConstructionTypeExt
		# """construction type of under crossing: bridge or tunnel"""
		self.___belongsToParent : tRef = tRef.tRef()
		# @AssociationType Common.tRef
		# """reference to a parent under crossing"""
		self.___allowedWeightLimit : tElementWithIDref = tElementWithIDref.tElementWithIDref()
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to weight limit classes that are allowed to pass over this under crossing"""
		self.___length : Length = Length.Length()
		# @AssociationType Infrastructure.Length*
		# @AssociationMultiplicity 0..*
		# """length of the under crossing relative to the railway in metres"""
		self.___unnamed_aVerbalConstraint_ : aVerbalConstraint = aVerbalConstraint.aVerbalConstraint()

