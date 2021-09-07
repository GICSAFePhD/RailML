#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tElementWithIDref
from RailML.Infrastructure import tBorderTypeExt, TrackNode
from typing import List, NewType

Long = NewType("Long", int)

class Border(TrackNode.TrackNode):
	"""A border point is used to separate the railway network due to different reasons. Typical examples are country borders, the change of owning infrastructure manager or the border of a station."""
	@property
	def IsOpenEnd(self) -> Long:
		return self.___isOpenEnd
	@property
	def ExternalRef(self) -> str:
		return self.___externalRef
	@property
	def Type(self) -> tBorderTypeExt:
		return self.___type
	@property
	def Id(self) -> tElementWithIDref:
		return self.___id

	@IsOpenEnd.setter
	def IsOpenEnd(self, aIsOpenEnd : Long):
		self.___isOpenEnd = aIsOpenEnd
	@ExternalRef.setter
	def ExternalRef(self, aExternalRef : str):
		self.___externalRef = aExternalRef
	@Type.setter
	def Type(self, aType : tBorderTypeExt):
		self.___type = aType
	@Id.setter
	def Id(self, aId : tElementWithIDref):
		self.___id = aId

	def create_Type(self):
		self.Type = tBorderTypeExt.tBorderTypeExt()
	def create_Id(self):
		self.Type = tElementWithIDref.tElementWithIDref()
	
	def __init__(self):
		super().__init__()
		self.___isOpenEnd : Long = 0
		"""set TRUE if this represents the end of the known network; default value FALSE"""
		self.___externalRef : str = ""
		"""reference to an external identifier allowing to connect in this border point (only useful in case of open ends)"""
		self.___type : tBorderTypeExt = None
		# @AssociationType Infrastructure.tBorderTypeExt
		# """defines the type of the border, e.g. "infrastructureManager" to indicate a border between two railway areas owned by different railway infrastructure managers"""
		self.___id : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to a functional infrastructure element that marks the border"""