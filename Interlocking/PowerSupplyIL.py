#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import tSignalVoltageModes
from Interlocking import EntityIL
from typing import List

class PowerSupplyIL(EntityIL):
	"""Interlocking specific features of the power supply"""
	def setNumberOfSimultaneousSwitchingActuators(self, aNumberOfSimultaneousSwitchingActuators : nonNegativeInteger):
		self.___numberOfSimultaneousSwitchingActuators = aNumberOfSimultaneousSwitchingActuators

	def getNumberOfSimultaneousSwitchingActuators(self) -> nonNegativeInteger:
		return self.___numberOfSimultaneousSwitchingActuators

	def setSignalVoltageMode(self, aSignalVoltageMode : tSignalVoltageModes):
		self.___signalVoltageMode = aSignalVoltageMode

	def getSignalVoltageMode(self) -> tSignalVoltageModes:
		return self.___signalVoltageMode

	def __init__(self):
		self.___numberOfSimultaneousSwitchingActuators : nonNegativeInteger = None
		"""maximum number of switch actuators that can be activated simultaneously with this power supply"""
		self.___signalVoltageMode : tSignalVoltageModes = None
		# @AssociationType Interlocking.tSignalVoltageModes
		# """mode of switching signal voltage for day and night voltage"""

