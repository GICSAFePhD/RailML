#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef, tElementWithIDref
from RailML.Infrastructure import tLineCategoryExt, tLineType, Length, LineTrafficCode, LineCombinedTransportCode, LineLayout, LinePerformance, FunctionalInfrastructureEntity
from typing import List

class Line(FunctionalInfrastructureEntity.FunctionalInfrastructureEntity):
	"""A line is a sequence of one or more line sections forming a route, which connects operational points and which may consist of several tracks used for regular railway operation."""
	@property
	def InfrastructureManagerRef(self) -> tRef:
		return self.___infrastructureManagerRef
	@property
	def LineCategory(self) -> tLineCategoryExt:
		return self.___lineCategory
	@property
	def LineType(self) -> tLineType:
		return self.___lineType
	@property
	def BelongsToParent(self) -> tRef:
		return self.___belongsToParent
	@property
	def BasedOnTemplate(self) -> tRef:
		return self.___basedOnTemplate
	@property
	def BeginsInOP(self) -> tElementWithIDref:
		return self.___beginsInOP
	@property
	def EndsInOP(self) -> tElementWithIDref:
		return self.___endsInOP
	@property
	def Length(self) -> Length:
		return self.___length
	@property
	def LineTrafficCode(self) -> LineTrafficCode:
		return self.___lineTrafficCode
	@property
	def LineCombinedTransportCode(self) -> LineCombinedTransportCode:
		return self.___lineCombinedTransportCode
	@property
	def LineLayout(self) -> LineLayout:
		return self.___lineLayout
	@property
	def LinePerformance(self) -> LinePerformance:
		return self.___linePerformance

	@InfrastructureManagerRef.setter
	def InfrastructureManagerRef(self, aInfrastructureManagerRef : tRef):
		self.___infrastructureManagerRef = aInfrastructureManagerRef
	@LineCategory.setter
	def LineCategory(self, aLineCategory : tLineCategoryExt):
		self.___lineCategory = aLineCategory
	@LineType.setter
	def LineType(self, aLineType : tLineType):
		self.___lineType = aLineType
	@BelongsToParent.setter
	def BelongsToParent(self, aBelongsToParent : tRef):
		self.___belongsToParent = aBelongsToParent
	@BasedOnTemplate.setter
	def BasedOnTemplate(self, aBasedOnTemplate : tRef):
		self.___basedOnTemplate = aBasedOnTemplate
	@BeginsInOP.setter
	def BeginsInOP(self, aBeginsInOP : tElementWithIDref):
		self.___beginsInOP = aBeginsInOP
	@EndsInOP.setter
	def EndsInOP(self, aEndsInOP : tElementWithIDref):
		self.___endsInOP = aEndsInOP
	@Length.setter
	def Length(self, aLength : Length):
		self.___length = aLength
	@LineTrafficCode.setter
	def LineTrafficCode(self, aLineTrafficCode : LineTrafficCode):
		self.___lineTrafficCode = aLineTrafficCode
	@LineCombinedTransportCode.setter
	def LineCombinedTransportCode(self, aLineCombinedTransportCode : LineCombinedTransportCode):
		self.___lineCombinedTransportCode = aLineCombinedTransportCode
	@LineLayout.setter
	def LineLayout(self, aLineLayout : LineLayout):
		self.___lineLayout = aLineLayout
	@LinePerformance.setter
	def LinePerformance(self, aLinePerformance : LinePerformance):
		self.___linePerformance = aLinePerformance

	def __init__(self):
		self.___infrastructureManagerRef : tRef = None
		"""reference to the infrastructure manager who owns the line (section) (see common/organizationalUnits)"""
		self.___lineCategory : tLineCategoryExt = None
		# @AssociationType Infrastructure.tLineCategoryExt
		# """the category of the line according to the EU regulation EN 15528 (A, B1, B2, C2, ..., E5; other national values are also possible)"""
		self.___lineType : tLineType =None
		# @AssociationType Infrastructure.tLineType
		# """this attribute is for distinguishing between main line and branch lines"""
		self.___belongsToParent : tRef = None
		# @AssociationType Common.tRef
		# """reference to the (one and only) parent line (section)"""
		self.___basedOnTemplate : tRef = None
		# @AssociationType Common.tRef
		# @AssociationType Common.tRef
		# """reference to a generic line (section)"""
		self.___beginsInOP : tElementWithIDref = None
		"""reference to the operational point where the line (section) begins"""
		self.___endsInOP : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref
		# @AssociationMultiplicity 0..1
		# @AssociationType Common.tElementWithIDref
		# @AssociationMultiplicity 0..1
		# """reference to the operational point where the line (section) ends"""
		self.___length : Length = None
		# @AssociationType Infrastructure.Length*
		# @AssociationMultiplicity 0..*
		# """length of the line (section)"""
		self.___lineTrafficCode : LineTrafficCode = None
		# @AssociationType Infrastructure.LineTrafficCode*
		# @AssociationMultiplicity 0..*
		# """TSI category of line as defined in TSI INF section 4.2.1; There should be one code for each type of traffic (passenger, freight) allowed on that line"""
		self.___lineCombinedTransportCode : LineCombinedTransportCode = None
		# @AssociationType Infrastructure.LineCombinedTransportCode*
		# @AssociationMultiplicity 0..*
		# """standard combined transport profile number as defined in UIC Code 596-6"""
		self.___lineLayout : LineLayout = None
		# @AssociationType Infrastructure.LineLayout
		# @AssociationMultiplicity 0..1
		# """child element summarizing the line layout parameters"""
		self.___linePerformance : LinePerformance = None
		# @AssociationType Infrastructure.LinePerformance
		# @AssociationMultiplicity 0..1
		# """child element summarizing the line performance parameters"""

