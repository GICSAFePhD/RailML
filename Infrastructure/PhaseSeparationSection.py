#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tLengthM import tLengthM
from typing import List

class PhaseSeparationSection(object):
	def setLengthPhaseSeparation(self, aLengthPhaseSeparation : tLengthM):
		self.___lengthPhaseSeparation = aLengthPhaseSeparation

	def getLengthPhaseSeparation(self) -> tLengthM:
		return self.___lengthPhaseSeparation

	def setSwitchOffBreaker(self, aSwitchOffBreaker : int):	#TODO DEFINED AS LONG
		self.___switchOffBreaker = aSwitchOffBreaker

	def getSwitchOffBreaker(self) -> int:	#TODO DEFINED AS LONG
		return self.___switchOffBreaker

	def setLowerPantograph(self, aLowerPantograph : int): #TODO DEFINED AS LONG
		self.___lowerPantograph = aLowerPantograph

	def getLowerPantograph(self) -> int:	#TODO DEFINED AS LONG
		return self.___lowerPantograph

	def __init__(self):
		self.___lengthPhaseSeparation : tLengthM = None
		# @AssociationType Common.tLengthM
		# """length of the phase separation section in contact line, in [m]"""
		self.___switchOffBreaker : int = None	#TODO DEFINED AS LONG
		"""flag, whether the main circuit breaker has to be switched off when passing the phase separation"""
		self.___lowerPantograph : int = None	#TODO DEFINED AS LONG
		"""flag, whether the pantographs have to be lowered when passing the phase separation"""

