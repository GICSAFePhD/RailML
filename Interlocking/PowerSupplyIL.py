#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.tSignalVoltageModes import tSignalVoltageModes
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class PowerSupplyIL(EntityIL):
	"""Interlocking specific features of the power supply"""
	def setNumberOfSimultaneousSwitchingActuators(self, aNumberOfSimultaneousSwitchingActuators : int):	#TODO DEFINED AS nonNegativeInteger
		self.___numberOfSimultaneousSwitchingActuators = aNumberOfSimultaneousSwitchingActuators

	def getNumberOfSimultaneousSwitchingActuators(self) -> int:	#TODO DEFINED AS nonNegativeInteger
		return self.___numberOfSimultaneousSwitchingActuators

	def setSignalVoltageMode(self, aSignalVoltageMode : tSignalVoltageModes):
		self.___signalVoltageMode = aSignalVoltageMode

	def getSignalVoltageMode(self) -> tSignalVoltageModes:
		return self.___signalVoltageMode

	def __init__(self):
		self.___numberOfSimultaneousSwitchingActuators : int = None	#TODO DEFINED AS nonNegativeInteger
		"""maximum number of switch actuators that can be activated simultaneously with this power supply"""
		self.___signalVoltageMode : tSignalVoltageModes = None
		# @AssociationType Interlocking.tSignalVoltageModes
		# """mode of switching signal voltage for day and night voltage"""

