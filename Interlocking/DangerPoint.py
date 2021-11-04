#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tLengthM, tSpeedKmPerHour
from RailML.Interlocking import EntityILref, RouteExit, EntityIL
from typing import List

class DangerPoint(EntityIL.EntityIL):
	"""The danger point defines the position beyond the exit signal up to where a train is likely to be safe.
	Designed for ETCS modelling."""
	@property
	def Distance(self) -> tLengthM:
		return self.___distance
	@property
	def ReleaseSpeed(self) -> tSpeedKmPerHour:
		return self.___releaseSpeed
	@property
	def LastSupervisedSectionBeforeDP(self) -> EntityILref:
		return self.___lastSupervisedSectionBeforeDP
	@property
	def SituatedAtTrackAsset(self) -> EntityILref:
		return self.___situatedAtTrackAsset
	@property
	def Unnamed_RouteExit_(self) -> RouteExit:
		return self.___unnamed_RouteExit_

	@Distance.setter
	def Distance(self, aDistance : tLengthM):
		self.___distance = aDistance
	@ReleaseSpeed.setter
	def ReleaseSpeed(self, aReleaseSpeed : tSpeedKmPerHour):
		self.___releaseSpeed = aReleaseSpeed
	@LastSupervisedSectionBeforeDP.setter
	def LastSupervisedSectionBeforeDP(self, aLastSupervisedSectionBeforeDP : EntityILref):
		self.___lastSupervisedSectionBeforeDP = aLastSupervisedSectionBeforeDP
	@SituatedAtTrackAsset.setter
	def SituatedAtTrackAsset(self, aSituatedAtTrackAsset : EntityILref):
		self.___situatedAtTrackAsset = aSituatedAtTrackAsset
	@Unnamed_RouteExit_.setter
	def Unnamed_RouteExit_(self, aUnnamed_RouteExit_ : RouteExit):
		self.___unnamed_RouteExit_ = aUnnamed_RouteExit_

	def create_LastSupervisedSectionBeforeDP(self):
		self.LastSupervisedSectionBeforeDP = EntityILref.EntityILref()
	def create_SituatedAtTrackAsset(self):
		self.SituatedAtTrackAsset = EntityILref.EntityILref()

	def __init__(self):
		super().__init__()
		self.___distance : tLengthM = None
		# @AssociationType Common.tLengthM
		# """Distance in metres from exit signal to danger point. Optional because one may also derive this distance from the track asset where the danger point is situated."""
		self.___releaseSpeed : tSpeedKmPerHour = None
		# @AssociationType Common.tSpeedKmPerHour
		# """Release speed in km/h associated with the danger point."""
		self.___lastSupervisedSectionBeforeDP : EntityILref = None
		"""This is the reference to last TVD section which is completely before the danger point. It is used when the danger point is situated at the end of a TVD section."""
		self.___situatedAtTrackAsset : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# """This is the reference to the track asset the danger point is located. It is used when the danger point is situated in the middle of a TVD section or beyond any TVD section in case of not supervised tracks."""
		self.___unnamed_RouteExit_ : RouteExit =None