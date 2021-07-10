#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tLengthM
from typing import List

class PhaseSeparationSection(object):
	def setLengthPhaseSeparation(self, aLengthPhaseSeparation : tLengthM):
		self.___lengthPhaseSeparation = aLengthPhaseSeparation

	def getLengthPhaseSeparation(self) -> tLengthM:
		return self.___lengthPhaseSeparation

	def setSwitchOffBreaker(self, aSwitchOffBreaker : long):
		self.___switchOffBreaker = aSwitchOffBreaker

	def getSwitchOffBreaker(self) -> long:
		return self.___switchOffBreaker

	def setLowerPantograph(self, aLowerPantograph : long):
		self.___lowerPantograph = aLowerPantograph

	def getLowerPantograph(self) -> long:
		return self.___lowerPantograph

	def __init__(self):
		self.___lengthPhaseSeparation : tLengthM = None
		# @AssociationType Common.tLengthM
		# """length of the phase separation section in contact line, in [m]"""
		self.___switchOffBreaker : long = None
		"""flag, whether the main circuit breaker has to be switched off when passing the phase separation"""
		self.___lowerPantograph : long = None
		"""flag, whether the pantographs have to be lowered when passing the phase separation"""

