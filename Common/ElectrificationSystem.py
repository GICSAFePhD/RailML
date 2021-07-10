#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tVoltageVolt
from Common import tFrequencyHertz
from Common import tElementWithID
from typing import List

class ElectrificationSystem(tElementWithID):
	def setVoltage(self, aVoltage : tVoltageVolt):
		self.___voltage = aVoltage

	def getVoltage(self) -> tVoltageVolt:
		return self.___voltage

	def setFrequency(self, aFrequency : tFrequencyHertz):
		self.___frequency = aFrequency

	def getFrequency(self) -> tFrequencyHertz:
		return self.___frequency

	def __init__(self):
		self.___voltage : tVoltageVolt = None
		# @AssociationType Common.tVoltageVolt
		# """electrification system voltage, in [V]"""
		self.___frequency : tFrequencyHertz = None
		# @AssociationType Common.tFrequencyHertz
		# """electrification system frequency, in [Hz]; for DC the frequency shall be set to zero"""

