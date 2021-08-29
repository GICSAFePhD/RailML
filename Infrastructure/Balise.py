#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef
from RailML.Infrastructure import tBaliseType, tBaliseGroupTypeExt,FunctionalInfrastructureEntity

from typing import List, NewType

Long = NewType("Long", int)

class Balise(FunctionalInfrastructureEntity.FunctionalInfrastructureEntity):
	@property
	def Type(self) -> tBaliseType:
		return self.___type
	@property
	def BelongsToParent(self) -> tRef:
		return self.___belongsToParent
	@property
	def BasedOnTemplate(self) -> tRef:
		return self.___basedOnTemplate
	@property
	def IsBaliseGroup(self) -> Long:
		return self.___isBaliseGroup
	@property
	def BaliseGroupType(self) -> tBaliseGroupTypeExt:
		return self.___baliseGroupType

	@Type.setter
	def Type(self, atBaliseType : tBaliseType):
		self.___type = atBaliseType
	@BelongsToParent.setter
	def BelongsToParent(self, atRef : tRef):
		self.___belongsToParent = atRef
	@BasedOnTemplate.setter
	def BasedOnTemplate(self, atRef : tRef):
		self.___basedOnTemplate = atRef
	@IsBaliseGroup.setter
	def IsBaliseGroup(self, aLong : Long):
		self.___isBaliseGroup = aLong
	@BaliseGroupType.setter
	def BaliseGroupType(self, atBaliseGroupTypeExt : tBaliseGroupTypeExt):
		self.___baliseGroupType = atBaliseGroupTypeExt

	def create_Type(self):
		self.Type = tBaliseType.tBaliseType()
	def create_BelongsToParent(self):
		self.BelongsToParent = tRef.tRef()
	def create_BasedOnTemplate(self):
		self.BasedOnTemplate = tRef.tRef() 
	def create_BaliseGroupType(self):
		self.BaliseGroupType = tBaliseGroupTypeExt.tBaliseGroupTypeExt()
    
	def __init__(self):
		self.___type : tBaliseType = None
		# @AssociationType Infrastructure.tBaliseType
		# """type of balise: fixed or transparent"""
		self.___belongsToParent : tRef = None
		"""reference to the (one and only) parent balise (group)"""
		self.___basedOnTemplate : tRef = None
		# @AssociationType Common.tRef
		# @AssociationType Common.tRef
		# """reference to a generic balise (group)"""
		self.___isBaliseGroup : Long = 0
		"""indicate whether the <balise> represents a balise group"""
		self.___baliseGroupType : tBaliseGroupTypeExt = None
		# @AssociationType Infrastructure.tBaliseGroupTypeExt
		# """type of balise group: fixed, transparent or infill"""