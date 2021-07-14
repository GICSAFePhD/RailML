#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.tCrossingConstructionTypeExt import tCrossingConstructionTypeExt
from RailML.Common.tRef import tRef
from RailML.Common.tElementWithIDref import tElementWithIDref
from RailML.Infrastructure.Length import Length
#from RailML.Infrastructure.aVerbalConstraint import aVerbalConstraint #TODO CIRCULAR!
from RailML.Infrastructure.XCrossing import XCrossing
from typing import List

class UnderCrossing(XCrossing):
	"""An under crossing describes a crossing, where something crosses under the railway line. The most common constructional type of an under crossing is a bridge."""
	def setConstructionType(self, aConstructionType : tCrossingConstructionTypeExt):
		self.___constructionType = aConstructionType

	def getConstructionType(self) -> tCrossingConstructionTypeExt:
		return self.___constructionType

	def setBelongsToParent(self, aBelongsToParent : tRef):
		self.___belongsToParent = aBelongsToParent

	def getBelongsToParent(self) -> tRef:
		return self.___belongsToParent

	def setAllowedWeightLimit(self, *aAllowedWeightLimit : tElementWithIDref):
		self._allowedWeightLimit = aAllowedWeightLimit

	def getAllowedWeightLimit(self) -> tElementWithIDref:
		return self._allowedWeightLimit

	def setLength(self, *aLength : Length):
		self._length = aLength

	def getLength(self) -> Length:
		return self._length

	def __init__(self):
		self.___constructionType : tCrossingConstructionTypeExt = None
		# @AssociationType Infrastructure.tCrossingConstructionTypeExt
		# """construction type of under crossing: bridge or tunnel"""
		self.___belongsToParent : tRef = None
		# @AssociationType Common.tRef
		# """reference to a parent under crossing"""
		self._allowedWeightLimit : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to weight limit classes that are allowed to pass over this under crossing"""
		self._length : Length = None
		# @AssociationType Infrastructure.Length*
		# @AssociationMultiplicity 0..*
		# """length of the under crossing relative to the railway in metres"""
		#self._unnamed_aVerbalConstraint_ : aVerbalConstraint = None	#TODO CIRCULAR!

