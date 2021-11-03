#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import PowerSupplyIL
from typing import List

class PowerSuppliesIL(object):
	"""container element for all PowerSupplyIL elements"""
	@property
	def PowerSupplyIL(self) -> PowerSupplyIL:
		return self.___powerSupplyIL
	
	@PowerSupplyIL.setter
	def PowerSupplyIL(self, aPowerSupplyIL : PowerSupplyIL):	# *aPowerSupplyIL
		self.___powerSupplyIL = aPowerSupplyIL

	def create_PowerSupplyIL(self):
		if self.PowerSupplyIL == None:
			self.PowerSupplyIL = []
		self.PowerSupplyIL.append(PowerSupplyIL.PowerSupplyIL())

	def __init__(self):
		self.___powerSupplyIL : PowerSupplyIL = None
		# @AssociationType Interlocking.PowerSupplyIL*
		# @AssociationMultiplicity 1..*
		# """specific features of power supply used for interlocking"""