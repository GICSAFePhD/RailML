#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tVoltageVolt, tFrequencyHertz, tElementWithID

from typing import List

class ElectrificationSystem(tElementWithID.tElementWithID):
	@property
	def tVoltageVolt(self) -> tVoltageVolt:
		return self.___voltage
	@property
	def tFrequencyHertz(self) -> tFrequencyHertz:
		return self.___frequency

	@tVoltageVolt.setter
	def tVoltageVolt(self, atVoltageVolt : tVoltageVolt):
		self.___voltage = atVoltageVolt
	@tFrequencyHertz.setter
	def tFrequencyHertz(self, atFrequencyHertz : tFrequencyHertz):
		self.___frequency = atFrequencyHertz

	def __init__(self):
		self.___voltage : tVoltageVolt = tVoltageVolt.tVoltageVolt()
		# @AssociationType Common.tVoltageVolt
		# """electrification system voltage, in [V]"""
		self.___frequency : tFrequencyHertz = tFrequencyHertz.tFrequencyHertz()
		# @AssociationType Common.tFrequencyHertz
		# """electrification system frequency, in [Hz]; for DC the frequency shall be set to zero"""

