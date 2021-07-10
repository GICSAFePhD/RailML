#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import TrainDetectionElement
from typing import List

class TrainDetectionElements(object):
	def setTrainDetectionElement(self, *aTrainDetectionElement : TrainDetectionElement*):
		self._trainDetectionElement = aTrainDetectionElement

	def getTrainDetectionElement(self) -> TrainDetectionElement*:
		return self._trainDetectionElement

	def __init__(self):
		self._trainDetectionElement : TrainDetectionElement = None
		# @AssociationType Infrastructure.TrainDetectionElement*
		# @AssociationMultiplicity 0..*

