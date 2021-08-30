#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef, tLengthM, tElementWithIDref
from RailML.Infrastructure import Length, FunctionalInfrastructureEntity
from typing import List

class Platform(FunctionalInfrastructureEntity.FunctionalInfrastructureEntity):
	@property
	def BelongsToParent(self) -> tRef:
		return self.___belongsToParent
	@property
	def BasedOnTemplate(self) -> tRef:
		return self.___basedOnTemplate
	@property
	def Height(self) -> tLengthM:
		return self.___height
	@property
	def OwnsPlatformEdge(self) -> tElementWithIDref:
		return self.___ownsPlatformEdge
	@property
	def Width(self) -> Length:
		return self.___width
	@property
	def Length(self) -> Length:
		return self.___length

	@BelongsToParent.setter
	def BelongsToParent(self, aBelongsToParent : tRef):
		self.___belongsToParent = aBelongsToParent
	@BasedOnTemplate.setter
	def BasedOnTemplate(self, aBasedOnTemplate : tRef):
		self.___basedOnTemplate = aBasedOnTemplate
	@Height.setter
	def Height(self, aHeight : tLengthM):
		self.___height = aHeight
	@OwnsPlatformEdge.setter
	def OwnsPlatformEdge(self, *aOwnsPlatformEdge : tLengthM):
		self.___ownsPlatformEdge = aOwnsPlatformEdge
	@Width.setter
	def Width(self, *aWidth : Length):
		self.___width = aWidth
	@Length.setter
	def Length(self, *aLength : Length):
		self.___length = aLength

	def create_OwnsPlatformEdge(self):
		if self.OwnsPlatformEdge == None:
			self.OwnsPlatformEdge = []
		self.OwnsPlatformEdge.append(tElementWithIDref.tElementWithIDref())
	def create_Width(self):
		if self.Width == None:
			self.Width = []
		self.Width.append(Length.Length())
	def create_Length(self):
		if self.Length == None:
			self.Length = []
		self.Length.append(Length.Length())

	def __init__(self):
		super().__init__()
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
		self.___ownsPlatformEdge : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to platform edge that belongs to this platform"""
		self.___width : Length = None
		"""width of the platform"""
		self.___length : Length = None
		# @AssociationType Infrastructure.Length*
		# @AssociationMultiplicity 0..*
		# @AssociationType Infrastructure.Length*
		# @AssociationMultiplicity 0..*
		# """length of the platform (edge)"""

