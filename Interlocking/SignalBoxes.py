#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import SignalBox
from typing import List

class SignalBoxes(object):
	"""container element for all signalBox elements"""
	def setSignalBox(self, *aSignalBox : SignalBox*):
		self._signalBox = aSignalBox

	def getSignalBox(self) -> SignalBox*:
		return self._signalBox

	def __init__(self):
		self._signalBox : SignalBox = None
		# @AssociationType Interlocking.SignalBox*
		# @AssociationMultiplicity 1..*
		# """Container with the characteristics of an individual interlocking system."""

