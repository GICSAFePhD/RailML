#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import EntityILref, EntityIL
from typing import List, NewType
Duration = NewType("Duration", int)

class LevelCrossingDeactivator(EntityIL.EntityIL):
	"""The train detector and/or TVD section(s) that deactivates the level crossing. This may be the level crossing tracks, e.g. km 12.809/2, that would appear on signalling plans."""
	@property
	def Delay(self) -> Duration:
		return self.___delay
	@property
	def TvdDetectorRef(self) -> EntityILref:
		return self.___tvdDetectorRef

	@Delay.setter
	def Delay(self, aDelay : Duration):
		self.___delay = aDelay
	@TvdDetectorRef.setter
	def TvdDetectorRef(self, aTvdDetectorRef : EntityILref):
		self.___tvdDetectorRef = aTvdDetectorRef

	def __init__(self):
		super().__init__()
		self.___delay : Duration = None
		"""Deactivation can be delayed by this timer. Starts counting when the associated TVD section is vacated."""
		self.___tvdDetectorRef : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the train detection element in infrastructure or a dedicated TVD section."""