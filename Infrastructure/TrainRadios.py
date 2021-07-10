#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import TrainRadio
from typing import List

class TrainRadios(object):
	"""umbrella element for all trainRadio elements"""
	def setTrainRadio(self, *aTrainRadio : TrainRadio*):
		self._trainRadio = aTrainRadio

	def getTrainRadio(self) -> TrainRadio*:
		return self._trainRadio

	def __init__(self):
		self._trainRadio : TrainRadio = None
		# @AssociationType Infrastructure.TrainRadio*
		# @AssociationMultiplicity 1..*

