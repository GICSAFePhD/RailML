#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import EntityILref
from Interlocking import EntityIL
from typing import List

class LevelCrossingDeactivator(EntityIL):
	"""The train detector and/or TVD section(s) that deactivates the level crossing. This may be the level crossing tracks, e.g. km 12.809/2, that would appear on signalling plans."""
	def setDelay(self, aDelay : duration):
		self.___delay = aDelay

	def getDelay(self) -> duration:
		return self.___delay

	def setTvdDetectorRef(self, aTvdDetectorRef : EntityILref):
		self._tvdDetectorRef = aTvdDetectorRef

	def getTvdDetectorRef(self) -> EntityILref:
		return self._tvdDetectorRef

	def __init__(self):
		self.___delay : duration = None
		"""Deactivation can be delayed by this timer. Starts counting when the associated TVD section is vacated."""
		self._tvdDetectorRef : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the train detection element in infrastructure or a dedicated TVD section."""

