#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import PowerSupplyIL
from typing import List

class PowerSuppliesIL(object):
	"""container element for all PowerSupplyIL elements"""
	def setPowerSupplyIL(self, *aPowerSupplyIL : PowerSupplyIL*):
		self._powerSupplyIL = aPowerSupplyIL

	def getPowerSupplyIL(self) -> PowerSupplyIL*:
		return self._powerSupplyIL

	def __init__(self):
		self._powerSupplyIL : PowerSupplyIL = None
		# @AssociationType Interlocking.PowerSupplyIL*
		# @AssociationMultiplicity 1..*
		# """specific features of power supply used for interlocking"""

