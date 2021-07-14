#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.TrackGauge import TrackGauge
from typing import List

class TrackGauges(object):
	"""umbrella element for all trackGauge elements"""
	def setTrackGauge(self, *aTrackGauge : TrackGauge):
		self._trackGauge = aTrackGauge

	def getTrackGauge(self) -> TrackGauge:
		return self._trackGauge

	def __init__(self):
		self._trackGauge : TrackGauge = None
		# @AssociationType Infrastructure.TrackGauge*
		# @AssociationMultiplicity 1..*

