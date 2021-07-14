#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.FunctionalInfrastructureEntity import FunctionalInfrastructureEntity
from typing import List

class LoadingGauge(FunctionalInfrastructureEntity):
	"""The loading gauge describes the maximum height and width for railway vehicles and their loads to ensure safe passage through bridges, tunnels and other structures."""
	def setCode(self, aCode : str):
		self.___code = aCode

	def getCode(self) -> str:
		return self.___code

	def __init__(self):
		self.___code : str = None
		"""code name of the train loading gauge;
		use value from the separate codelist file 'TrainClearanceGauges.xml'/trainClearanceGauge"""

