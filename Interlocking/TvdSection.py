#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tFrequencyHertz
from RailML.Interlocking import tTvdSectionTechnologyTypeExt, EntityILref, TrackAsset
from typing import List, NewType
Long = NewType("Long", int)
Duration = NewType("Duration", int)

class TvdSection(TrackAsset.TrackAsset):
	"""A track vacancy detection (TVD) section reports train occupancy to the interlocking. This is a logical unit characterised by the delimiters of the section. Typically, a section is delimited by two insulated track joints or axle counters at the extremities. Sections with a switch or a crossing can have several such limits."""
	@property
	def IsBerthingTrack(self) -> Long:
		return self.___isBerthingTrack
	@property
	def ResidualRouteCancellationDelay(self) -> Duration:
		return self.___residualRouteCancellationDelay
	@property
	def PartialRouteReleaseDelay(self) -> Duration:
		return self.___partialRouteReleaseDelay
	@property
	def Technology(self) -> tTvdSectionTechnologyTypeExt:
		return self.___technology
	@property
	def Frequency(self) -> tFrequencyHertz:
		return self.___frequency
	@property
	def HasDemarcatingBufferstop(self) -> EntityILref:
		return self.___hasDemarcatingBufferstop
	@property
	def HasExitSignal(self) -> EntityILref:
		return self.___hasExitSignal
	@property
	def HasDemarcatingTraindetector(self) -> EntityILref:
		return self.___hasDemarcatingTraindetector
	@property
	def HasResetStrategy(self) -> EntityILref:
		return self.___hasResetStrategy

	@IsBerthingTrack.setter
	def IsBerthingTrack(self, aIsBerthingTrack : Long):
		self.___isBerthingTrack = aIsBerthingTrack
	@ResidualRouteCancellationDelay.setter
	def ResidualRouteCancellationDelay(self, aResidualRouteCancellationDelay : Duration):
		self.___residualRouteCancellationDelay = aResidualRouteCancellationDelay
	@PartialRouteReleaseDelay.setter
	def PartialRouteReleaseDelay(self, aPartialRouteReleaseDelay : Duration):
		self.___partialRouteReleaseDelay = aPartialRouteReleaseDelay
	@Technology.setter
	def Technology(self, aTechnology : tTvdSectionTechnologyTypeExt):
		self.___technology = aTechnology
	@Frequency.setter
	def Frequency(self, aFrequency : tFrequencyHertz):
		self.___frequency = aFrequency
	@HasDemarcatingBufferstop.setter
	def HasDemarcatingBufferstop(self, aHasDemarcatingBufferstop : EntityILref): # TODO *aHasDemarcatingBufferstop
		self.___hasDemarcatingBufferstop = aHasDemarcatingBufferstop
	@HasExitSignal.setter
	def HasExitSignal(self, aHasExitSignal : EntityILref): # TODO *aHasExitSignal
		self.___hasExitSignal = aHasExitSignal
	@HasDemarcatingTraindetector.setter
	def HasDemarcatingTraindetector(self, aHasDemarcatingTraindetector : EntityILref):
		self.___hasDemarcatingTraindetector = aHasDemarcatingTraindetector
	@HasResetStrategy.setter
	def HasResetStrategy(self, aHasResetStrategy : EntityILref): # TODO *aHasResetStrategy
		self.___hasResetStrategy = aHasResetStrategy

	def create_HasDemarcatingBufferstop(self):
		if self.HasDemarcatingBufferstop == None:
			self.HasDemarcatingBufferstop = []
		self.HasDemarcatingBufferstop.append(EntityILref.EntityILref())
	def create_HasExitSignal(self):
		if self.HasExitSignal == None:
			self.HasExitSignal = []
		self.HasExitSignal.append(EntityILref.EntityILref())
	def create_HasDemarcatingTraindetector(self):
		if self.HasDemarcatingTraindetector == None:
			self.HasDemarcatingTraindetector = []
		self.HasDemarcatingTraindetector.append(EntityILref.EntityILref())
	def create_HasResetStrategy(self):
		if self.HasResetStrategy == None:
			self.HasResetStrategy = []
		self.HasResetStrategy.append(EntityILref.EntityILref())

	def __init__(self):
		super().__init__()
		self.___isBerthingTrack : Long = 0
		"""True if this section is part of a berthing track, i.e. track where trains may halt and change direction. Typically, an Interlocking assures that trains progress from section to section in an ordered sequence (aka. two/three phase release). This check would fail when a train changes direction. If this attribute is true, the interlocking doesn't carry out this check for this section."""
		self.___residualRouteCancellationDelay : Duration = 0
		"""The delay after which the interlocking may clear a partial route left by an unusual train run. The timer starts running when the interlocking accepts the signal man request to clear the section (DE: Restfahrstrasse aufl�sen) or when the interlocking algorithm detects that the train has set back (automatic route release)."""
		self.___partialRouteReleaseDelay : Duration = 0
		"""Delay time after which the section may be released for use in a new route"""
		self.___technology : tTvdSectionTechnologyTypeExt = None
		# @AssociationType Interlocking.tTvdSectionTechnologyTypeExt
		# """the technical type of the TVD section"""
		self.___frequency : tFrequencyHertz = None
		# @AssociationType Common.tFrequencyHertz
		# """The frequency in Hertz in case of a track circuit. Shall be zero for direct current."""
		self.___hasDemarcatingBufferstop : EntityILref = None
		"""Reference to physical track ends, e.g. buffer stop."""
		self.___hasExitSignal : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """Reference to delimiting signals for leaving the TVD section."""
		self.___hasDemarcatingTraindetector : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# """Reference to the physical train detection points, e.g. axle counter point, insulated rail joint."""
		self.___hasResetStrategy : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..2
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..2
		# """Reference to the IM specific reset strategy for this TVD section."""