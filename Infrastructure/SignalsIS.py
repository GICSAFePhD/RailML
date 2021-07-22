#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import SignalIS
from typing import List

class SignalsIS(object):
	@property
	def SignalIS(self) -> SignalIS:
		return self.___signalIS
	
	@SignalIS.setter
	def SignalIS(self, *aSignalIS : SignalIS):
		self.___signalIS = aSignalIS

	def __init__(self):
		self.___signalIS : SignalIS = SignalIS.SignalIS()
		# @AssociationType Infrastructure.SignalIS*
		# @AssociationMultiplicity 1..*

