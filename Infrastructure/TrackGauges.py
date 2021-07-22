#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import TrackGauge
from typing import List

class TrackGauges(object):
	"""umbrella element for all trackGauge elements"""
	@property
	def TrackGauge(self) -> TrackGauge:
		return self.___trackGauge
	
	@TrackGauge.setter
	def TrackGauge(self, *aTrackGauge : TrackGauge):
		self.___trackGauge = aTrackGauge

	def __init__(self):
		self.___trackGauge : TrackGauge = TrackGauge.TrackGauge()
		# @AssociationType Infrastructure.TrackGauge*
		# @AssociationMultiplicity 1..*

