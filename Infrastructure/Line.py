#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tRef import tRef
from RailML.Infrastructure.tLineCategoryExt import tLineCategoryExt
from RailML.Infrastructure.tLineType import tLineType
from RailML.Common.tElementWithIDref import tElementWithIDref
from RailML.Infrastructure.Length import Length
from RailML.Infrastructure.LineTrafficCode import LineTrafficCode
from RailML.Infrastructure.LineCombinedTransportCode import LineCombinedTransportCode
from RailML.Infrastructure.LineLayout import LineLayout
from RailML.Infrastructure.LinePerformance import LinePerformance
from RailML.Infrastructure.FunctionalInfrastructureEntity import FunctionalInfrastructureEntity
from typing import List

class Line(FunctionalInfrastructureEntity):
	"""A line is a sequence of one or more line sections forming a route, which connects operational points and which may consist of several tracks used for regular railway operation."""
	def setInfrastructureManagerRef(self, aInfrastructureManagerRef : tRef):
		self.___infrastructureManagerRef = aInfrastructureManagerRef

	def getInfrastructureManagerRef(self) -> tRef:
		return self.___infrastructureManagerRef

	def setLineCategory(self, aLineCategory : tLineCategoryExt):
		self.___lineCategory = aLineCategory

	def getLineCategory(self) -> tLineCategoryExt:
		return self.___lineCategory

	def setLineType(self, aLineType : tLineType):
		self.___lineType = aLineType

	def getLineType(self) -> tLineType:
		return self.___lineType

	def setBelongsToParent(self, aBelongsToParent : tRef):
		self.___belongsToParent = aBelongsToParent

	def getBelongsToParent(self) -> tRef:
		return self.___belongsToParent

	def setBasedOnTemplate(self, aBasedOnTemplate : tRef):
		self.___basedOnTemplate = aBasedOnTemplate

	def getBasedOnTemplate(self) -> tRef:
		return self.___basedOnTemplate

	def setBeginsInOP(self, aBeginsInOP : tElementWithIDref):
		self._beginsInOP = aBeginsInOP

	def getBeginsInOP(self) -> tElementWithIDref:
		return self._beginsInOP

	def setEndsInOP(self, aEndsInOP : tElementWithIDref):
		self._endsInOP = aEndsInOP

	def getEndsInOP(self) -> tElementWithIDref:
		return self._endsInOP

	def setLength(self, *aLength : Length):
		self._length = aLength

	def getLength(self) -> Length:
		return self._length

	def setLineTrafficCode(self, *aLineTrafficCode : LineTrafficCode):
		self._lineTrafficCode = aLineTrafficCode

	def getLineTrafficCode(self) -> LineTrafficCode:
		return self._lineTrafficCode

	def setLineCombinedTransportCode(self, *aLineCombinedTransportCode : LineCombinedTransportCode):
		self._lineCombinedTransportCode = aLineCombinedTransportCode

	def getLineCombinedTransportCode(self) -> LineCombinedTransportCode:
		return self._lineCombinedTransportCode

	def setLineLayout(self, aLineLayout : LineLayout):
		self._lineLayout = aLineLayout

	def getLineLayout(self) -> LineLayout:
		return self._lineLayout

	def setLinePerformance(self, aLinePerformance : LinePerformance):
		self._linePerformance = aLinePerformance

	def getLinePerformance(self) -> LinePerformance:
		return self._linePerformance

	def __init__(self):
		self.___infrastructureManagerRef : tRef = None
		"""reference to the infrastructure manager who owns the line (section) (see common/organizationalUnits)"""
		self.___lineCategory : tLineCategoryExt = None
		# @AssociationType Infrastructure.tLineCategoryExt
		# """the category of the line according to the EU regulation EN 15528 (A, B1, B2, C2, ..., E5; other national values are also possible)"""
		self.___lineType : tLineType = None
		# @AssociationType Infrastructure.tLineType
		# """this attribute is for distinguishing between main line and branch lines"""
		self.___belongsToParent : tRef = None
		# @AssociationType Common.tRef
		# """reference to the (one and only) parent line (section)"""
		self.___basedOnTemplate : tRef = None
		# @AssociationType Common.tRef
		# @AssociationType Common.tRef
		# """reference to a generic line (section)"""
		self._beginsInOP : tElementWithIDref = None
		"""reference to the operational point where the line (section) begins"""
		self._endsInOP : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref
		# @AssociationMultiplicity 0..1
		# @AssociationType Common.tElementWithIDref
		# @AssociationMultiplicity 0..1
		# """reference to the operational point where the line (section) ends"""
		self._length : Length = None
		# @AssociationType Infrastructure.Length*
		# @AssociationMultiplicity 0..*
		# """length of the line (section)"""
		self._lineTrafficCode : LineTrafficCode = None
		# @AssociationType Infrastructure.LineTrafficCode*
		# @AssociationMultiplicity 0..*
		# """TSI category of line as defined in TSI INF section 4.2.1; There should be one code for each type of traffic (passenger, freight) allowed on that line"""
		self._lineCombinedTransportCode : LineCombinedTransportCode = None
		# @AssociationType Infrastructure.LineCombinedTransportCode*
		# @AssociationMultiplicity 0..*
		# """standard combined transport profile number as defined in UIC Code 596-6"""
		self._lineLayout : LineLayout = None
		# @AssociationType Infrastructure.LineLayout
		# @AssociationMultiplicity 0..1
		# """child element summarizing the line layout parameters"""
		self._linePerformance : LinePerformance = None
		# @AssociationType Infrastructure.LinePerformance
		# @AssociationMultiplicity 0..1
		# """child element summarizing the line performance parameters"""

