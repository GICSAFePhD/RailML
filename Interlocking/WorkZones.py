#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import WorkZone
from typing import List

class WorkZones(object):
	@property
	def WorkZone(self) -> WorkZone:
		return self.___workZone
	
	@WorkZone.setter
	def WorkZone(self, *aWorkZone : WorkZone):
		self.___workZone = aWorkZone

	def __init__(self):
		self.___workZone : WorkZone = WorkZone.WorkZone()
		# @AssociationType Interlocking.WorkZone*
		# @AssociationMultiplicity 1..*
		# """A set of track assets that track workers or the signalman can set apart from the main line."""

