#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.tContactState import tContactState
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class InputOutput(EntityIL):
	"""The detailed list of input or output information (closed=1=active, open=0=inactive)"""
	def setBitNr(self, aBitNr : int):	#TODO DEFINED AS nonNegativeInteger
		self.___bitNr = aBitNr

	def getBitNr(self) -> int:	#TODO DEFINED AS nonNegativeInteger
		return self.___bitNr

	def setDescription(self, aDescription : str):
		self.___description = aDescription

	def getDescription(self) -> str:
		return self.___description

	def setNormalState(self, aNormalState : tContactState):
		self.___normalState = aNormalState

	def getNormalState(self) -> tContactState:
		return self.___normalState

	def setPulseDuration(self, aPulseDuration : int):	#TODO DEFINED AS duration
		self.___pulseDuration = aPulseDuration

	def getPulseDuration(self) -> int:	#TODO DEFINED AS duration
		return self.___pulseDuration

	def __init__(self):
		self.___bitNr : int = None	#TODO DEFINED AS nonNegativeInteger
		"""The order number of the information."""
		self.___description : str = None
		"""The verbal description of the information."""
		self.___normalState : tContactState = None
		# @AssociationType Interlocking.tContactState
		# """The power-off state of the input or output."""
		self.___pulseDuration : int = None	#TODO DEFINED AS duration
		"""The pulse width of the input or output if using pulsed information."""

