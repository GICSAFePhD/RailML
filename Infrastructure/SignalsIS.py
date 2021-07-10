#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import SignalIS
from typing import List

class SignalsIS(object):
	def setSignalIS(self, *aSignalIS : SignalIS*):
		self._signalIS = aSignalIS

	def getSignalIS(self) -> SignalIS*:
		return self._signalIS

	def __init__(self):
		self._signalIS : SignalIS = None
		# @AssociationType Infrastructure.SignalIS*
		# @AssociationMultiplicity 1..*

