#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tRef import tRef
from RailML.Infrastructure.aServiceSection import aServiceSection
from RailML.Infrastructure.FunctionalInfrastructureEntity import FunctionalInfrastructureEntity
from typing import List

class ServiceSection(FunctionalInfrastructureEntity):
	def setBelongsToParent(self, aBelongsToParent : tRef):
		self.___belongsToParent = aBelongsToParent

	def getBelongsToParent(self) -> tRef:
		return self.___belongsToParent

	def __init__(self):
		self.___belongsToParent : tRef = None
		# @AssociationType Common.tRef
		# """reference to the (one and only) parent service section"""
		self._unnamed_aServiceSection_ : aServiceSection = None

