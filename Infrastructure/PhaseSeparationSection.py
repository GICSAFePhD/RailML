#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tLengthM
from typing import List, NewType
Long = NewType("Long", int)

class PhaseSeparationSection(object):
	@property
	def LengthPhaseSeparation(self) -> tLengthM:
		return self.___lengthPhaseSeparation
	@property
	def SwitchOffBreaker(self) -> Long:
		return self.___switchOffBreaker
	@property
	def LowerPantograph(self) -> Long:
		return self.___lowerPantograph

	@LengthPhaseSeparation.setter
	def LengthPhaseSeparation(self, aLengthPhaseSeparation : tLengthM):
		self.___lengthPhaseSeparation = aLengthPhaseSeparation
	@SwitchOffBreaker.setter
	def SwitchOffBreaker(self, aSwitchOffBreaker : Long):
		self.___switchOffBreaker = aSwitchOffBreaker
	@LowerPantograph.setter
	def LowerPantograph(self, aLowerPantograph : Long):
		self.___lowerPantograph = aLowerPantograph

	def __init__(self):
		self.___lengthPhaseSeparation : tLengthM = tLengthM.tLengthM()
		# @AssociationType Common.tLengthM
		# """length of the phase separation section in contact line, in [m]"""
		self.___switchOffBreaker : Long = 0
		"""flag, whether the main circuit breaker has to be switched off when passing the phase separation"""
		self.___lowerPantograph : Long = 0	
		"""flag, whether the pantographs have to be lowered when passing the phase separation"""

