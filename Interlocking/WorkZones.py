#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import WorkZone
from typing import List

class WorkZones(object):
	def setWorkZone(self, *aWorkZone : WorkZone*):
		self._workZone = aWorkZone

	def getWorkZone(self) -> WorkZone*:
		return self._workZone

	def __init__(self):
		self._workZone : WorkZone = None
		# @AssociationType Interlocking.WorkZone*
		# @AssociationMultiplicity 1..*
		# """A set of track assets that track workers or the signalman can set apart from the main line."""

