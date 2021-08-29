#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import TrainRadio
from typing import List

class TrainRadios(object):
	"""umbrella element for all trainRadio elements"""
	@property
	def TrainRadio(self) -> TrainRadio:
		return self.___trainRadio
	
	@TrainRadio.setter
	def TrainRadio(self, *aTrainRadio : TrainRadio):
		self.___trainRadio = aTrainRadio

	def create_TrainRadio(self):
		if self.TrainRadio == None:
			self.TrainRadio = []
		self.TrainRadio.append(TrainRadio.TrainRadio())

	def __init__(self):
		self.___trainRadio : TrainRadio = None
		# @AssociationType Infrastructure.TrainRadio*
		# @AssociationMultiplicity 1..*

