#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import TrainRadio
from typing import List

class TrainRadios(object):
	"""umbrella element for all trainRadio elements"""
	@property
	def TrainRadio(self) -> TrainRadio:
		return self.___gradientCurve
	
	@TrainRadio.setter
	def TrainRadio(self, *aTrainRadio : TrainRadio):
		self.___gradientCurve = aTrainRadio

	def __init__(self):
		self.___trainRadio : TrainRadio = TrainRadio.TrainRadio()
		# @AssociationType Infrastructure.TrainRadio*
		# @AssociationMultiplicity 1..*

