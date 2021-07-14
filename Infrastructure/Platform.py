#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tRef import tRef
from RailML.Common.tLengthM import tLengthM
from RailML.Common.tElementWithIDref import tElementWithIDref
from RailML.Infrastructure.Length import Length
from RailML.Infrastructure.FunctionalInfrastructureEntity import FunctionalInfrastructureEntity
from typing import List

class Platform(FunctionalInfrastructureEntity):
	def setBelongsToParent(self, aBelongsToParent : tRef):
		self.___belongsToParent = aBelongsToParent

	def getBelongsToParent(self) -> tRef:
		return self.___belongsToParent

	def setBasedOnTemplate(self, aBasedOnTemplate : tRef):
		self.___basedOnTemplate = aBasedOnTemplate

	def getBasedOnTemplate(self) -> tRef:
		return self.___basedOnTemplate

	def setHeight(self, aHeight : tLengthM):
		self.___height = aHeight

	def getHeight(self) -> tLengthM:
		return self.___height

	def setOwnsPlatformEdge(self, *aOwnsPlatformEdge : tElementWithIDref):
		self._ownsPlatformEdge = aOwnsPlatformEdge

	def getOwnsPlatformEdge(self) -> tElementWithIDref:
		return self._ownsPlatformEdge

	def setWidth(self, *aWidth : Length):
		self._width = aWidth

	def getWidth(self) -> Length:
		return self._width

	def setLength(self, *aLength : Length):
		self._length = aLength

	def getLength(self) -> Length:
		return self._length

	def __init__(self):
		self.___belongsToParent : tRef = None
		"""reference to a parent platform (edge);
		use this attribute for grouping of platform edges with different parameters (e.g. different heights)"""
		self.___basedOnTemplate : tRef = None
		# @AssociationType Common.tRef
		# @AssociationType Common.tRef
		# """reference to a template platform (edge)"""
		self.___height : tLengthM = None
		# @AssociationType Common.tLengthM
		# """the height of the platform edge in metres"""
		self._ownsPlatformEdge : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to platform edge that belongs to this platform"""
		self._width : Length = None
		"""width of the platform"""
		self._length : Length = None
		# @AssociationType Infrastructure.Length*
		# @AssociationMultiplicity 0..*
		# @AssociationType Infrastructure.Length*
		# @AssociationMultiplicity 0..*
		# """length of the platform (edge)"""

