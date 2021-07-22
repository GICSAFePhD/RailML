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

	def __init__(self):
		self.___loadingGauge : LoadingGauge = LoadingGauge.LoadingGauge()
		# @AssociationType Infrastructure.LoadingGauge*
		# @AssociationMultiplicity 1..*

