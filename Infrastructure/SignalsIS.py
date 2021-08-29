#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import SignalIS
from typing import List

class SignalsIS(object):
	@property
	def SignalIS(self) -> SignalIS:
		return self.___signalIS
	
	@SignalIS.setter
	def SignalIS(self, aSignalIS : SignalIS):	#TODO *aSignalIS
		self.___signalIS = aSignalIS

	def create_SignalIS(self):
		if self.SignalIS == None:
			self.SignalIS = []
		self.SignalIS.append(SignalIS.SignalIS())

	def __init__(self):
		self.___signalIS : SignalIS = None
		# @AssociationType Infrastructure.SignalIS*
		# @AssociationMultiplicity 1..*

