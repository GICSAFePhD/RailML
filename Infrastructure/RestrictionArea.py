#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import tRestrictionAreaTypeExt, FunctionalInfrastructureEntity
from typing import List

class RestrictionArea(FunctionalInfrastructureEntity.FunctionalInfrastructureEntity):
	@property
	def Type(self) -> tRestrictionAreaTypeExt:
		return self.___type
	
	@Type.setter
	def Type(self, atRestrictionAreaTypeExt : tRestrictionAreaTypeExt):
		self.___type = atRestrictionAreaTypeExt

	def __init__(self):
		self.___type : tRestrictionAreaTypeExt = None
		# @AssociationType Infrastructure.tRestrictionAreaTypeExt
		# """type of restriction that applies in the restriction area (for most values see UNISIG Subset 026, chapter 7.5.1.77 M_TRACKCOND)"""

