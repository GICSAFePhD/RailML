#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tLengthM import tLengthM
from typing import List

class SystemSeparationSection(object):
	def setLengthSystemSeparation(self, aLengthSystemSeparation : tLengthM):
		self.___lengthSystemSeparation = aLengthSystemSeparation

	def getLengthSystemSeparation(self) -> tLengthM:
		return self.___lengthSystemSeparation

	def setSwitchOffBreaker(self, aSwitchOffBreaker : int): #TODO DEFINED AS LONG
		self.___switchOffBreaker = aSwitchOffBreaker

	def getSwitchOffBreaker(self) -> int:	#TODO DEFINED AS LONG
		return self.___switchOffBreaker

	def setLowerPantograph(self, aLowerPantograph : int):	#TODO DEFINED AS LONG
		self.___lowerPantograph = aLowerPantograph

	def getLowerPantograph(self) -> int:	#TODO DEFINED AS LONG
		return self.___lowerPantograph

	def setIsSupplySystemChange(self, aIsSupplySystemChange : int):	#TODO DEFINED AS LONG
		self.___isSupplySystemChange = aIsSupplySystemChange

	def getIsSupplySystemChange(self) -> int:	#TODO DEFINED AS LONG
		return self.___isSupplySystemChange

	def __init__(self):
		self.___lengthSystemSeparation : tLengthM = None
		# @AssociationType Common.tLengthM
		# """length of the system separation section in contact line, in [m]"""
		self.___switchOffBreaker : int = None	#TODO DEFINED AS LONG
		"""flag, whether the main circuit breaker has to be switched off when passing the system separation"""
		self.___lowerPantograph : int = None	#TODO DEFINED AS LONG
		"""flag, whether the pantographs have to be lowered when passing the system separation"""
		self.___isSupplySystemChange : int = None	#TODO DEFINED AS LONG
		"""flag, whether the supply system changes at the separation"""

