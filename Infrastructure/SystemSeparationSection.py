#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tLengthM
from typing import List, NewType
Long = NewType("Long", int)

class SystemSeparationSection(object):
	@property
	def LengthSystemSeparation(self) -> tLengthM:
		return self.___lengthSystemSeparation
	@property
	def SwitchOffBreaker(self) -> Long:
		return self.___switchOffBreaker
	@property
	def LowerPantograph(self) -> Long:
		return self.___lowerPantograph
	@property
	def IsSupplySystemChange(self) -> Long:
		return self.___isSupplySystemChange

	@LengthSystemSeparation.setter
	def LengthSystemSeparation(self, aLengthSystemSeparation : tLengthM):
		self.___lengthSystemSeparation = aLengthSystemSeparation
	@SwitchOffBreaker.setter
	def SwitchOffBreaker(self, aSwitchOffBreaker : Long):
		self.___switchOffBreaker = aSwitchOffBreaker
	@LowerPantograph.setter
	def LowerPantograph(self, aLowerPantograph : Long):
		self.___lowerPantograph = aLowerPantograph
	@IsSupplySystemChange.setter
	def IsSupplySystemChange(self, aIsSupplySystemChange : Long):
		self.___isSupplySystemChange = aIsSupplySystemChange

	def __init__(self):
		self.___lengthSystemSeparation : tLengthM = tLengthM.tLengthM()
		# @AssociationType Common.tLengthM
		# """length of the system separation section in contact line, in [m]"""
		self.___switchOffBreaker : Long = 0
		"""flag, whether the main circuit breaker has to be switched off when passing the system separation"""
		self.___lowerPantograph : Long = 0
		"""flag, whether the pantographs have to be lowered when passing the system separation"""
		self.___isSupplySystemChange : Long = 0
		"""flag, whether the supply system changes at the separation"""

