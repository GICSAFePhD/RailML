#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import Track
from typing import List

class Tracks(object):
	@property
	def Track(self) -> Track:
		return self.___track
	
	@Track.setter
	def Track(self, *aTrack : Track):
		self.___track = aTrack

	def __init__(self):
		self.___track : Track = Track.Track()
		# @AssociationType Infrastructure.Track*
		# @AssociationMultiplicity 1..*

