#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import tTvdSectionTechnologyTypeExt
from Common import tFrequencyHertz
from Interlocking import EntityILref
from Interlocking import TrackAsset
from typing import List

class TvdSection(TrackAsset):
	"""A track vacancy detection (TVD) section reports train occupancy to the interlocking. This is a logical unit characterised by the delimiters of the section. Typically, a section is delimited by two insulated track joints or axle counters at the extremities. Sections with a switch or a crossing can have several such limits."""
	def setIsBerthingTrack(self, aIsBerthingTrack : long):
		self.___isBerthingTrack = aIsBerthingTrack

	def getIsBerthingTrack(self) -> long:
		return self.___isBerthingTrack

	def setResidualRouteCancellationDelay(self, aResidualRouteCancellationDelay : duration):
		self.___residualRouteCancellationDelay = aResidualRouteCancellationDelay

	def getResidualRouteCancellationDelay(self) -> duration:
		return self.___residualRouteCancellationDelay

	def setPartialRouteReleaseDelay(self, aPartialRouteReleaseDelay : duration):
		self.___partialRouteReleaseDelay = aPartialRouteReleaseDelay

	def getPartialRouteReleaseDelay(self) -> duration:
		return self.___partialRouteReleaseDelay

	def setTechnology(self, aTechnology : tTvdSectionTechnologyTypeExt):
		self.___technology = aTechnology

	def getTechnology(self) -> tTvdSectionTechnologyTypeExt:
		return self.___technology

	def setFrequency(self, aFrequency : tFrequencyHertz):
		self.___frequency = aFrequency

	def getFrequency(self) -> tFrequencyHertz:
		return self.___frequency

	def setHasDemarcatingBufferstop(self, *aHasDemarcatingBufferstop : EntityILref*):
		self._hasDemarcatingBufferstop = aHasDemarcatingBufferstop

	def getHasDemarcatingBufferstop(self) -> EntityILref*:
		return self._hasDemarcatingBufferstop

	def setHasExitSignal(self, *aHasExitSignal : EntityILref*):
		self._hasExitSignal = aHasExitSignal

	def getHasExitSignal(self) -> EntityILref*:
		return self._hasExitSignal

	def setHasDemarcatingTraindetector(self, aHasDemarcatingTraindetector : EntityILref):
		self._hasDemarcatingTraindetector = aHasDemarcatingTraindetector

	def getHasDemarcatingTraindetector(self) -> EntityILref:
		return self._hasDemarcatingTraindetector

	def setHasResetStrategy(self, *aHasResetStrategy : EntityILref*):
		self._hasResetStrategy = aHasResetStrategy

	def getHasResetStrategy(self) -> EntityILref*:
		return self._hasResetStrategy

	def __init__(self):
		self.___isBerthingTrack : long = None
		"""True if this section is part of a berthing track, i.e. track where trains may halt and change direction. Typically, an Interlocking assures that trains progress from section to section in an ordered sequence (aka. two/three phase release). This check would fail when a train changes direction. If this attribute is true, the interlocking doesn't carry out this check for this section."""
		self.___residualRouteCancellationDelay : duration = None
		"""The delay after which the interlocking may clear a partial route left by an unusual train run. The timer starts running when the interlocking accepts the signal man request to clear the section (DE: Restfahrstrasse auflösen) or when the interlocking algorithm detects that the train has set back (automatic route release)."""
		self.___partialRouteReleaseDelay : duration = None
		"""Delay time after which the section may be released for use in a new route"""
		self.___technology : tTvdSectionTechnologyTypeExt = None
		# @AssociationType Interlocking.tTvdSectionTechnologyTypeExt
		# """the technical type of the TVD section"""
		self.___frequency : tFrequencyHertz = None
		# @AssociationType Common.tFrequencyHertz
		# """The frequency in Hertz in case of a track circuit. Shall be zero for direct current."""
		self._hasDemarcatingBufferstop : EntityILref = None
		"""Reference to physical track ends, e.g. buffer stop."""
		self._hasExitSignal : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """Reference to delimiting signals for leaving the TVD section."""
		self._hasDemarcatingTraindetector : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# """Reference to the physical train detection points, e.g. axle counter point, insulated rail joint."""
		self._hasResetStrategy : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..2
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..2
		# """Reference to the IM specific reset strategy for this TVD section."""

