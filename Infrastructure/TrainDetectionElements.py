#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.TrainDetectionElement import TrainDetectionElement
from typing import List

class TrainDetectionElements(object):
	@property
	def TrainDetectionElement(self) -> TrainDetectionElement:
		return self.___trainDetectionElement
	
	@TrainDetectionElement.setter
	def TrainDetectionElement(self, *aTrainDetectionElement : TrainDetectionElement):
		self.___trainDetectionElement = aTrainDetectionElement

	def __init__(self):
		self.___trainDetectionElement : TrainDetectionElement = None
		# @AssociationType Infrastructure.TrainDetectionElement*
		# @AssociationMultiplicity 0..*

