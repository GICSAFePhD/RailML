#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.Overlap import Overlap
from typing import List

class Overlaps(object):
	"""container element for all Overlap elements"""
	def setOverlap(self, *aOverlap : Overlap):
		self._overlap = aOverlap

	def getOverlap(self) -> Overlap:
		return self._overlap

	def __init__(self):
		self._overlap : Overlap = None
		# @AssociationType Interlocking.Overlap*
		# @AssociationMultiplicity 1..*
		# """track(s) in advance of a stop signal, or a stopping point in a continuous signalling system, which must be kept clear to avoid the risk of collision should a train inadvertently run past the signal or the stopping point"""

