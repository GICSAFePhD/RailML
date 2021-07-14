#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.tBorderTypeExt import tBorderTypeExt
from RailML.Common.tElementWithIDref import tElementWithIDref
from RailML.Infrastructure.TrackNode import TrackNode
from typing import List

class Border(TrackNode):
	"""A border point is used to separate the railway network due to different reasons. Typical examples are country borders, the change of owning infrastructure manager or the border of a station."""
	def setIsOpenEnd(self, aIsOpenEnd : int): #TODO DEFINED AS LONG
		self.___isOpenEnd = aIsOpenEnd

	def getIsOpenEnd(self) -> int:	#TODO DEFINED AS LONG
		return self.___isOpenEnd

	def setExternalRef(self, aExternalRef : str):
		self.___externalRef = aExternalRef

	def getExternalRef(self) -> str:
		return self.___externalRef

	def setType(self, aType : tBorderTypeExt):
		self.___type = aType

	def getType(self) -> tBorderTypeExt:
		return self.___type

	def setMarkedByInfrastructureElement(self, *aMarkedByInfrastructureElement : tElementWithIDref):
		self._markedByInfrastructureElement = aMarkedByInfrastructureElement

	def getMarkedByInfrastructureElement(self) -> tElementWithIDref:
		return self._markedByInfrastructureElement

	def __init__(self):
		self.___isOpenEnd : int = None	#TODO DEFINED AS LONG
		"""set TRUE if this represents the end of the known network; default value FALSE"""
		self.___externalRef : str = None
		"""reference to an external identifier allowing to connect in this border point (only useful in case of open ends)"""
		self.___type : tBorderTypeExt = None
		# @AssociationType Infrastructure.tBorderTypeExt
		# """defines the type of the border, e.g. "infrastructureManager" to indicate a border between two railway areas owned by different railway infrastructure managers"""
		self._markedByInfrastructureElement : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to a functional infrastructure element that marks the border"""

