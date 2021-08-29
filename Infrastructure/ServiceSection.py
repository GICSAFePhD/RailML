#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef
from RailML.Infrastructure import aServiceSection, FunctionalInfrastructureEntity
from typing import List

class ServiceSection(FunctionalInfrastructureEntity.FunctionalInfrastructureEntity):
	@property
	def BelongsToParent(self) -> tRef:
		return self.___belongsToParent
	@property
	def Unnamed_aServiceSection(self) -> aServiceSection:
		return self.___unnamed_aServiceSection_

	@BelongsToParent.setter
	def BelongsToParent(self, aBelongsToParent : tRef):
		self.___belongsToParent = aBelongsToParent
	@Unnamed_aServiceSection.setter
	def Unnamed_aServiceSection(self, aUnnamed_aServiceSection : aServiceSection):
		self.___unnamed_aServiceSection_ = aUnnamed_aServiceSection

	def __init__(self):
		self.___belongsToParent : tRef = None
		# @AssociationType Common.tRef
		# """reference to the (one and only) parent service section"""
		#self.___unnamed_aServiceSection_ : aServiceSection = aServiceSection.aServiceSection() #TODO FIX THIS

