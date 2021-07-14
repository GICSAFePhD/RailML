#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.LoadingGauge import LoadingGauge
from typing import List

class LoadingGauges(object):
	"""umbrella element for all loadingGauge elements"""
	def setLoadingGauge(self, *aLoadingGauge : LoadingGauge):
		self._loadingGauge = aLoadingGauge

	def getLoadingGauge(self) -> LoadingGauge:
		return self._loadingGauge

	def __init__(self):
		self._loadingGauge : LoadingGauge = None
		# @AssociationType Infrastructure.LoadingGauge*
		# @AssociationMultiplicity 1..*

