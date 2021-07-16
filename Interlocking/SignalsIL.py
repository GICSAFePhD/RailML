#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.SignalIL import SignalIL
from typing import List

class SignalsIL(object):
	"""container element for all SignalIL elements"""
	def setSignalIL(self, *aSignalIL : SignalIL):
		self._signalIL = aSignalIL

	def getSignalIL(self) -> SignalIL:
		return self._signalIL

	def __init__(self):
		self._signalIL : SignalIL = None
		# @AssociationType Interlocking.SignalIL*
		# @AssociationMultiplicity 1..*
		# """The signal is a track asset used to transmit information to the train driver represented by its optical appearance."""

