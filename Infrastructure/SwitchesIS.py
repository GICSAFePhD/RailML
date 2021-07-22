#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import SwitchIS
from typing import List

class SwitchesIS(object):
	@property
	def SwitchIS(self) -> SwitchIS:
		return self.___switchIS
	
	@SwitchIS.setter
	def SwitchIS(self, *aSwitchIS : SwitchIS):
		self.___switchIS = aSwitchIS

	def __init__(self):
		self.___switchIS : SwitchIS = SwitchIS.SwitchIS()
		# @AssociationType Infrastructure.SwitchIS*
		# @AssociationMultiplicity 1..*

