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

	def create_TrainProtectionElement(self):
		if self.TrainProtectionElement == None:
			self.TrainProtectionElement = []
		self.TrainProtectionElement.append(TrainProtectionElement.TrainProtectionElement())

	def __init__(self):
		self.___trainProtectionElement : TrainProtectionElement = None
		# @AssociationType Infrastructure.TrainProtectionElement*
		# @AssociationMultiplicity 0..*

