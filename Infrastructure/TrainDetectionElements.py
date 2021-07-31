#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import TrainDetectionElement
from typing import List

class TrainDetectionElements(object):
	@property
	@property
	def TrainDetectionElement(self) -> TrainDetectionElement:
		return self.___trainDetectionElement
	
	@TrainDetectionElement.setter
	def TrainDetectionElement(self, *aTrainDetectionElement : TrainDetectionElement):
		self.___trainDetectionElement = aTrainDetectionElement

	def __init__(self):
		self.___trainDetectionElement : TrainDetectionElement = TrainDetectionElement.TrainDetectionElement()
		# @AssociationType Infrastructure.TrainDetectionElement*
		# @AssociationMultiplicity 0..*

