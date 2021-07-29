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

	def __init__(self):
		self.___belongsToParent : tRef = tRef.tRef()
		"""reference to a parent platform (edge);
		use this attribute for grouping of platform edges with different parameters (e.g. different heights)"""
		self.___basedOnTemplate : tRef = tRef.tRef()
		# @AssociationType Common.tRef
		# @AssociationType Common.tRef
		# """reference to a template platform (edge)"""
		self.___height : tLengthM = tLengthM.tLengthM()
		# @AssociationType Common.tLengthM
		# """the height of the platform edge in metres"""
		self.___ownsPlatformEdge : tElementWithIDref = tElementWithIDref.tElementWithIDref()
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to platform edge that belongs to this platform"""
		self.___width : Length = Length.Length()
		"""width of the platform"""
		self.___length : Length = Length.Length()
		# @AssociationType Infrastructure.Length*
		# @AssociationMultiplicity 0..*
		# @AssociationType Infrastructure.Length*
		# @AssociationMultiplicity 0..*
		# """length of the platform (edge)"""

