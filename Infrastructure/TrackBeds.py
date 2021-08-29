#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import TrackBed
from typing import List

class TrackBeds(object):
	@property
	def TrackBed(self) -> TrackBed:
		return self.___trackBed
	
	@TrackBed.setter
	def TrackBed(self, *aTrackBed : TrackBed):
		self.___trackBed = aTrackBed

	def create_TrackBed(self):
		if self.TrackBed == None:
			self.TrackBed = []
		self.TrackBed.append(TrackBed.TrackBed())

	def __init__(self):
		self.___trackBed : TrackBed = None
		# @AssociationType Infrastructure.TrackBed*
		# @AssociationMultiplicity 1..*

