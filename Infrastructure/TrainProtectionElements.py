#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import TrainProtectionElement
from typing import List

class TrainProtectionElements(object):
	@property
	def TrainProtectionElement(self) -> TrainProtectionElement:
		return self.___trainProtectionElement
	
	@TrainProtectionElement.setter
	def TrainProtectionElement(self, *aTrainProtectionElement : TrainProtectionElement):
		self.___trainProtectionElement = aTrainProtectionElement

	def __init__(self):
		self.___trainProtectionElement : TrainProtectionElement = TrainProtectionElement.TrainProtectionElement()
		# @AssociationType Infrastructure.TrainProtectionElement*
		# @AssociationMultiplicity 0..*

