#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.tCrossingConstructionTypeExt import tCrossingConstructionTypeExt
from RailML.Common.tRef import tRef
from RailML.Common.tElementWithIDref import tElementWithIDref
from RailML.Infrastructure.Length import Length
#from RailML.Infrastructure.aVerbalConstraint import aVerbalConstraint #TODO CIRCULAR!
from RailML.Infrastructure.XCrossing import XCrossing
from typing import List

class OverCrossing(XCrossing):
	"""An over crossing describes a crossing, where something crosses over the railway line. From constructional point of view an over crossing can be a bridge or a tunnel."""
	def setConstructionType(self, aConstructionType : tCrossingConstructionTypeExt):
		self.___constructionType = aConstructionType

	def getConstructionType(self) -> tCrossingConstructionTypeExt:
		return self.___constructionType

	def setBelongsToParent(self, aBelongsToParent : tRef):
		self.___belongsToParent = aBelongsToParent

	def getBelongsToParent(self) -> tRef:
		return self.___belongsToParent

	def setAllowedLoadingGauge(self, *aAllowedLoadingGauge : tElementWithIDref):
		self._allowedLoadingGauge = aAllowedLoadingGauge

	def getAllowedLoadingGauge(self) -> tElementWithIDref:
		return self._allowedLoadingGauge

	def setLength(self, *aLength : Length):
		self._length = aLength

	def getLength(self) -> Length:
		return self._length

	def __init__(self):
		self.___constructionType : tCrossingConstructionTypeExt = None
		# @AssociationType Infrastructure.tCrossingConstructionTypeExt
		# """construction type of over crossing: bridge or tunnel"""
		self.___belongsToParent : tRef = None
		# @AssociationType Common.tRef
		# """reference to a parent over crossing"""
		self._allowedLoadingGauge : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to train clearance gauge classes that are allowed to pass through the over crossing"""
		self._length : Length = None
		# @AssociationType Infrastructure.Length*
		# @AssociationMultiplicity 0..*
		# """length of the over crossing relative to the railway in metres"""
		#self._unnamed_aVerbalConstraint_ : aVerbalConstraint = None #TODO CIRCULAR!

