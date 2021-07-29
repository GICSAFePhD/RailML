#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tElementWithIDref
from RailML.Infrastructure import SignalX
from typing import List

class SignalStopPost(SignalX.SignalX):
	@property
	def RefersToStoppingPlace(self) -> tElementWithIDref:
		return self.___refersToStoppingPlace
	
	@RefersToStoppingPlace.setter
	def RefersToStoppingPlace(self, aRefersToStoppingPlace : tElementWithIDref):
		self.___refersToStoppingPlace = aRefersToStoppingPlace

	def __init__(self):
		self.___refersToStoppingPlace : tElementWithIDref = tElementWithIDref.tElementWithIDref()
		# @AssociationType Common.tElementWithIDref
		# @AssociationMultiplicity 0..1
		# """reference to the stoppingPlace"""

