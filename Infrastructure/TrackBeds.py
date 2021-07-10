#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import TrackBed
from typing import List

class TrackBeds(object):
	def setTrackBed(self, *aTrackBed : TrackBed*):
		self._trackBed = aTrackBed

	def getTrackBed(self) -> TrackBed*:
		return self._trackBed

	def __init__(self):
		self._trackBed : TrackBed = None
		# @AssociationType Infrastructure.TrackBed*
		# @AssociationMultiplicity 1..*

