#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import TrackBed
from typing import List

class TrackBeds(object):
	@property
	def TrackBed(self) -> TrackBed:
		return self.___gradientCurve
	
	@TrackBed.setter
	def TrackBed(self, *aTrackBed : TrackBed):
		self.___gradientCurve = aTrackBed

	def __init__(self):
		self.___trackBed : TrackBed = TrackBed.TrackBed()
		# @AssociationType Infrastructure.TrackBed*
		# @AssociationMultiplicity 1..*

