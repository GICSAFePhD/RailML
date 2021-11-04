#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import FunctionalInfrastructureEntity
from typing import List

class LoadingGauge(FunctionalInfrastructureEntity.FunctionalInfrastructureEntity):
	"""The loading gauge describes the maximum height and width for railway vehicles and their loads to ensure safe passage through bridges, tunnels and other structures."""
	@property
	def Code(self) -> str:
		return self.___code
	
	@Code.setter
	def Code(self, aCode : str):
		self.___code = aCode

	def __init__(self):
		super().__init__()
		self.___code : str = None
		"""code name of the train loading gauge;
		use value from the separate codelist file 'TrainClearanceGauges.xml'/trainClearanceGauge"""