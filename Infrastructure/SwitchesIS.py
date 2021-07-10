#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import SwitchIS
from typing import List

class SwitchesIS(object):
	def setSwitchIS(self, *aSwitchIS : SwitchIS*):
		self._switchIS = aSwitchIS

	def getSwitchIS(self) -> SwitchIS*:
		return self._switchIS

	def __init__(self):
		self._switchIS : SwitchIS = None
		# @AssociationType Infrastructure.SwitchIS*
		# @AssociationMultiplicity 1..*

