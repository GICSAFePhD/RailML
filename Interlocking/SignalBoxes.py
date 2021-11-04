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
	def SignalBox(self, aSignalBox : SignalBox):	# TODO *aSignalBox
		self.___signalBox = aSignalBox

	def create_SignalBox(self):
		if self.SignalBox == None:
			self.SignalBox = []
		self.SignalBox.append(SignalBox.SignalBox())

	def __init__(self):
		self.___signalBox : SignalBox = None
		# @AssociationType Interlocking.SignalBox*
		# @AssociationMultiplicity 1..*
		# """Container with the characteristics of an individual interlocking system."""