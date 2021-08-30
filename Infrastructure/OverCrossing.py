#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef, tElementWithIDref
from RailML.Infrastructure import tCrossingConstructionTypeExt, Length, XCrossing, aVerbalConstraint

from typing import List

class OverCrossing(XCrossing.XCrossing):
	"""An over crossing describes a crossing, where something crosses over the railway line. From constructional point of view an over crossing can be a bridge or a tunnel."""	
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
		# """construction type of over crossing: bridge or tunnel"""
		self.___belongsToParent : tRef = None
		# @AssociationType Common.tRef
		# """reference to a parent over crossing"""
		self.___allowedLoadingGauge : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to train clearance gauge classes that are allowed to pass through the over crossing"""
		self.___length : Length = None
		# @AssociationType Infrastructure.Length*
		# @AssociationMultiplicity 0..*
		# """length of the over crossing relative to the railway in metres"""
		self.___unnamed_aVerbalConstraint_ : aVerbalConstraint = None

