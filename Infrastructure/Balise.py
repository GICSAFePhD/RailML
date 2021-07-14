#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.tBaliseType import tBaliseType
from RailML.Common.tRef import tRef
from RailML.Infrastructure.tBaliseGroupTypeExt import tBaliseGroupTypeExt
from RailML.Infrastructure.FunctionalInfrastructureEntity import FunctionalInfrastructureEntity
from typing import List

class Balise(FunctionalInfrastructureEntity):
	def setType(self, aType : tBaliseType):
		self.___type = aType

	def getType(self) -> tBaliseType:
		return self.___type

	def setBelongsToParent(self, aBelongsToParent : tRef):
		self.___belongsToParent = aBelongsToParent

	def getBelongsToParent(self) -> tRef:
		return self.___belongsToParent

	def setBasedOnTemplate(self, aBasedOnTemplate : tRef):
		self.___basedOnTemplate = aBasedOnTemplate

	def getBasedOnTemplate(self) -> tRef:
		return self.___basedOnTemplate

	def setIsBaliseGroup(self, aIsBaliseGroup : int):	#TODO DEFINED AS LONG
		self.___isBaliseGroup = aIsBaliseGroup

	def getIsBaliseGroup(self) -> int:	#TODO DEFINED AS LONG
		return self.___isBaliseGroup

	def setBaliseGroupType(self, aBaliseGroupType : tBaliseGroupTypeExt):
		self.___baliseGroupType = aBaliseGroupType

	def getBaliseGroupType(self) -> tBaliseGroupTypeExt:
		return self.___baliseGroupType

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
		self.___isBaliseGroup : int = None		#TODO DEFINED AS LONG
		"""indicate whether the <balise> represents a balise group"""
		self.___baliseGroupType : tBaliseGroupTypeExt = None
		# @AssociationType Infrastructure.tBaliseGroupTypeExt
		# """type of balise group: fixed, transparent or infill"""

