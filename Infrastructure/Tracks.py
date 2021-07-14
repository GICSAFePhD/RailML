#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.Track import Track
from typing import List

class Tracks(object):
	def setTrack(self, *aTrack : Track):
		self._track = aTrack

	def getTrack(self) -> Track:
		return self._track

	def __init__(self):
		self._track : Track = None
		# @AssociationType Infrastructure.Track*
		# @AssociationMultiplicity 1..*

