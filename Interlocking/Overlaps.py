#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import Overlap
from typing import List

class Overlaps(object):
	"""container element for all Overlap elements"""
	@property
	def Overlap(self) -> Overlap:
		return self.___overlap
	
	@Overlap.setter
	def Overlap(self, *aOverlap : Overlap):
		self.___overlap = aOverlap

	def __init__(self):
		self.___overlap : Overlap = None
		# @AssociationType Interlocking.Overlap*
		# @AssociationMultiplicity 1..*
		# """track(s) in advance of a stop signal, or a stopping point in a continuous signalling system, which must be kept clear to avoid the risk of collision should a train inadvertently run past the signal or the stopping point"""