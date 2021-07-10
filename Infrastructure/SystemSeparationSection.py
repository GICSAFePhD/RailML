#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tLengthM
from typing import List

class SystemSeparationSection(object):
	def setLengthSystemSeparation(self, aLengthSystemSeparation : tLengthM):
		self.___lengthSystemSeparation = aLengthSystemSeparation

	def getLengthSystemSeparation(self) -> tLengthM:
		return self.___lengthSystemSeparation

	def setSwitchOffBreaker(self, aSwitchOffBreaker : long):
		self.___switchOffBreaker = aSwitchOffBreaker

	def getSwitchOffBreaker(self) -> long:
		return self.___switchOffBreaker

	def setLowerPantograph(self, aLowerPantograph : long):
		self.___lowerPantograph = aLowerPantograph

	def getLowerPantograph(self) -> long:
		return self.___lowerPantograph

	def setIsSupplySystemChange(self, aIsSupplySystemChange : long):
		self.___isSupplySystemChange = aIsSupplySystemChange

	def getIsSupplySystemChange(self) -> long:
		return self.___isSupplySystemChange

	def __init__(self):
		self.___lengthSystemSeparation : tLengthM = None
		# @AssociationType Common.tLengthM
		# """length of the system separation section in contact line, in [m]"""
		self.___switchOffBreaker : long = None
		"""flag, whether the main circuit breaker has to be switched off when passing the system separation"""
		self.___lowerPantograph : long = None
		"""flag, whether the pantographs have to be lowered when passing the system separation"""
		self.___isSupplySystemChange : long = None
		"""flag, whether the supply system changes at the separation"""

