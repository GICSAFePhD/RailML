#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import tRestrictionAreaTypeExt
from Infrastructure import FunctionalInfrastructureEntity
from typing import List

class RestrictionArea(FunctionalInfrastructureEntity):
	def setType(self, aType : tRestrictionAreaTypeExt):
		self.___type = aType

	def getType(self) -> tRestrictionAreaTypeExt:
		return self.___type

	def __init__(self):
		self.___type : tRestrictionAreaTypeExt = None
		# @AssociationType Infrastructure.tRestrictionAreaTypeExt
		# """type of restriction that applies in the restriction area (for most values see UNISIG Subset 026, chapter 7.5.1.77 M_TRACKCOND)"""

