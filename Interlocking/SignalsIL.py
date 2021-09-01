#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import SignalIL
from typing import List

class SignalsIL(object):
	"""container element for all SignalIL elements"""
	@property
	def SignalIL(self) -> SignalIL:
		return self.___signalIL
	
	@SignalIL.setter
	def SignalIL(self, *aSignalIL : SignalIL):
		self.___signalIL = aSignalIL

	def __init__(self):
		self.___signalIL : SignalIL = None
		# @AssociationType Interlocking.SignalIL*
		# @AssociationMultiplicity 1..*
		# """The signal is a track asset used to transmit information to the train driver represented by its optical appearance."""