#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tSignalVoltageModes, EntityIL
from typing import List, NewType

nonNegativeInteger = NewType("nonNegativeInteger", int)

class PowerSupplyIL(EntityIL.EntityIL):
	"""Interlocking specific features of the power supply"""
	@property
	def NumberOfSimultaneousSwitchingActuators(self) -> nonNegativeInteger:
		return self.___numberOfSimultaneousSwitchingActuators
	@property
	def SignalVoltageMode(self) -> tSignalVoltageModes:
		return self.___signalVoltageMode

	@NumberOfSimultaneousSwitchingActuators.setter
	def NumberOfSimultaneousSwitchingActuators(self, aNumberOfSimultaneousSwitchingActuators : nonNegativeInteger):
		self.___numberOfSimultaneousSwitchingActuators = aNumberOfSimultaneousSwitchingActuators
	@SignalVoltageMode.setter
	def SignalVoltageMode(self, aSignalVoltageMode : tSignalVoltageModes):
		self.___signalVoltageMode = aSignalVoltageMode

	def __init__(self):
		self.___numberOfSimultaneousSwitchingActuators : nonNegativeInteger = 0
		"""maximum number of switch actuators that can be activated simultaneously with this power supply"""
		self.___signalVoltageMode : tSignalVoltageModes = tSignalVoltageModes.tSignalVoltageModes()
		# @AssociationType Interlocking.tSignalVoltageModes
		# """mode of switching signal voltage for day and night voltage"""

