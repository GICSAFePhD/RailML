#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import Track
from typing import List

class Tracks(object):
	@property
	def Track(self) -> Track:
		return self.___track
	
	@Track.setter
	def Track(self, aTrack : Track): # TODO *aTrack
		self.___track = aTrack

	def create_Track(self):
		if self.Track == None:
			self.Track = []
		self.Track.append(Track.Track())

	def __init__(self):
		self.___track : Track = None
		# @AssociationType Infrastructure.Track*
		# @AssociationMultiplicity 1..*