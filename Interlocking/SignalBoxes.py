#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import SignalBox
from typing import List

class SignalBoxes(object):
	"""container element for all signalBox elements"""
	@property
	def SignalBox(self) -> SignalBox:
		return self.___signalBox
	
	@SignalBox.setter
	def SignalBox(self, *aSignalBox : SignalBox):
		self.___signalBox = aSignalBox

	def __init__(self):
		self.___signalBox : SignalBox = SignalBox.SignalBox()
		# @AssociationType Interlocking.SignalBox*
		# @AssociationMultiplicity 1..*
		# """Container with the characteristics of an individual interlocking system."""

