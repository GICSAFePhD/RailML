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

	def create_TrackGauge(self):
		if self.TrackGauge == None:
			self.TrackGauge = []
		self.TrackGauge.append(TrackGauge.TrackGauge())

	def __init__(self):
		self.___trackGauge : TrackGauge = None
		# @AssociationType Infrastructure.TrackGauge*
		# @AssociationMultiplicity 1..*

