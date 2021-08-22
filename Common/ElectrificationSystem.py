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


	def create_tVoltageVolt(self):
		self.tVoltageVolt = tVoltageVolt.tVoltageVolt()
	def create_tFrequencyHertz(self):
		self.tFrequencyHertz = tFrequencyHertz.tFrequencyHertz()

	def __init__(self):
		self.___voltage : tVoltageVolt = None
		# @AssociationType Common.tVoltageVolt
		# """electrification system voltage, in [V]"""
		self.___frequency : tFrequencyHertz = None
		# @AssociationType Common.tFrequencyHertz
		# """electrification system frequency, in [Hz]; for DC the frequency shall be set to zero"""

