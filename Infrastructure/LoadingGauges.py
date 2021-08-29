#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import LoadingGauge
from typing import List

class LoadingGauges(object):
	"""umbrella element for all loadingGauge elements"""
	@property
	def LoadingGauge(self) -> LoadingGauge:
		return self.___loadingGauge
	
	@LoadingGauge.setter
	def LoadingGauge(self, aLoadingGauge : LoadingGauge):
		self.___loadingGauge = aLoadingGauge

	def create_LoadingGauge(self):
		if self.LoadingGauge == None:
			self.LoadingGauge = []
		self.LoadingGauge.append(LoadingGauge.LoadingGauge())

	def __init__(self):
		self.___loadingGauge : LoadingGauge = None
		# @AssociationType Infrastructure.LoadingGauge*
		# @AssociationMultiplicity 1..*

