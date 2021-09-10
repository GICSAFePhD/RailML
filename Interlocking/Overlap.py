#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tSpeedKmPerHour, tLengthM
from RailML.Interlocking import EntityILref, LevelCrossingAndGivenState, OverlapRelease, RouteExit, EntityIL, SwitchAndGivenPosition
from typing import List, NewType
Duration = NewType("Duration", int)

class Overlap(EntityIL.EntityIL):
	"""INESS (INtegrated European Signalling System) definition: A defined section of track in advance of a stop signal, or a stopping point in a continuous signalling system, which must be kept clear to avoid the risk of collision should a train inadvertently run past the signal or the stopping point.
	Many IMs require overlap beyond active routes to protect from overshoot. One or more sections beyond the exit signal are locked out from use by other routes. The overlap is delimited by train detectors. Facing switches in the overlap are locked, otherwise, use the swinging overlap. Trailing switches in the overlap may normally not locked. Note that there is no need to explicitly identify the switches in the overlap because they can be derived from the begin and endpoints of the overlap.
	The overlap can be released if the RBC deems that an approaching train is slow enough such that overshoot is unlikely.
	Trains other than the one for which the route-overlap is locked may be attributed a permitted speed in the overlap. If the value is set to 0 it is not possible to set a route through the overlap. Compare this variable with the release speed that applies to the train that is being released beyond the danger point."""
	@property
	def ReleaseSpeed(self) -> tSpeedKmPerHour:
		return self.___releaseSpeed
	@property
	def OverlapSpeed(self) -> tSpeedKmPerHour:
		return self.___overlapSpeed
	@property
	def OverlapValidityTime(self) -> Duration:
		return self.___overlapValidityTime
	@property
	def Length(self) -> tLengthM:
		return self.___length
	@property
	def ActiveForApproachRoute(self) -> EntityILref:
		return self.___activeForApproachRoute
	@property
	def RelatedToTrackAsset(self) -> EntityILref:
		return self.___relatedToTrackAsset
	@property
	def RequiresSwitchInPosition(self) -> SwitchAndGivenPosition:
		return self.___requiresSwitchInPosition
	@property
	def RequiresLevelCrossingInState(self) -> LevelCrossingAndGivenState:
		return self.___requiresLevelCrossingInState
	@property
	def HasTvdSection(self) -> EntityILref:
		return self.___hasTvdSection
	@property
	def IsLimitedBy(self) -> EntityILref:
		return self.___isLimitedBy
	@property
	def OverlapRelease(self) -> OverlapRelease:
		return self.___overlapRelease
	#@property
	#def Unnamed_RouteExit_(self) -> RouteExit:
	#		return self.___unnamed_RouteExit_
	#@property
	#def RequiresPointInPosition(self) -> List:
	#	return self.___requiresPointInPosition
	#@property
	#def RequiresAssetInState(self) -> List:
	#	return self.___requiresAssetInState

	@ReleaseSpeed.setter
	def ReleaseSpeed(self, aReleaseSpeed : tSpeedKmPerHour):
		self.___releaseSpeed = aReleaseSpeed
	@OverlapSpeed.setter
	def OverlapSpeed(self, aOverlapSpeed : tSpeedKmPerHour):
		self.___overlapSpeed = aOverlapSpeed
	@OverlapValidityTime.setter
	def OverlapValidityTime(self, aOverlapValidityTime : Duration):
		self.___overlapValidityTime = aOverlapValidityTime
	@Length.setter
	def Length(self, aLength : tLengthM):
		self.___length = aLength
	@ActiveForApproachRoute.setter
	def ActiveForApproachRoute(self, aActiveForApproachRoute : EntityILref):
		self.___activeForApproachRoute = aActiveForApproachRoute
	@RelatedToTrackAsset.setter
	def RelatedToTrackAsset(self, aRelatedToTrackAsset : EntityILref): # TODO *aRelatedToTrackAsset
		self.___relatedToTrackAsset = aRelatedToTrackAsset
	@RequiresSwitchInPosition.setter
	def RequiresSwitchInPosition(self, aRequiresSwitchInPosition : SwitchAndGivenPosition): # TODO *aRequiresSwitchInPosition
		self.___requiresSwitchInPosition = aRequiresSwitchInPosition
	@RequiresLevelCrossingInState.setter
	def RequiresLevelCrossingInState(self, aRequiresLevelCrossingInState : LevelCrossingAndGivenState): # TODO *aRequiresLevelCrossingInState
		self.___requiresLevelCrossingInState = aRequiresLevelCrossingInState
	@HasTvdSection.setter
	def HasTvdSection(self, aHasTvdSection : EntityILref):	# TODO *aHasTvdSection
		self.___hasTvdSection = aHasTvdSection
	@IsLimitedBy.setter
	def IsLimitedBy(self, aIsLimitedBy : EntityILref):	# TODO *aIsLimitedBy
		self.___isLimitedBy = aIsLimitedBy
	@OverlapRelease.setter
	def OverlapRelease(self, aOverlapRelease : OverlapRelease):
		self.___overlapRelease = aOverlapRelease
	#@Unnamed_RouteExit_.setter
	#def Unnamed_RouteExit_(self, aUnnamed_RouteExit_ : RouteExit):
	#	self.___unnamed_RouteExit_ = aUnnamed_RouteExit_
	#@RequiresPointInPosition.setter
	#def RequiresPointInPosition(self, aRequiresPointInPosition : List):
	#	self.___requiresPointInPosition = aRequiresPointInPosition
	#@RequiresAssetInState.setter
	#def RequiresAssetInState(self, aRequiresAssetInState : List):
	#	self.___requiresAssetInState = aRequiresAssetInState

	def create_ActiveForApproachRoute(self):
		if self.ActiveForApproachRoute == None:
			self.ActiveForApproachRoute = []
		self.ActiveForApproachRoute.append(EntityILref.EntityILref())
	def create_RelatedToTrackAsset(self):
		self.RelatedToTrackAsset = EntityILref.EntityILref()
	def create_RequiresSwitchInPosition(self):
		if self.RequiresSwitchInPosition == None:
			self.RequiresSwitchInPosition = []
		self.RequiresSwitchInPosition.append(SwitchAndGivenPosition.SwitchAndGivenPosition())
	def create_RequiresLevelCrossingInState(self):
		if self.RequiresLevelCrossingInState == None:
			self.RequiresLevelCrossingInState = []
		self.RequiresLevelCrossingInState.append(LevelCrossingAndGivenState.LevelCrossingAndGivenState())
	def create_HasTvdSection(self):
		if self.HasTvdSection == None:
			self.HasTvdSection = []
		self.HasTvdSection.append(EntityILref.EntityILref())
	def create_IsLimitedBy(self):
		if self.IsLimitedBy == None:
			self.IsLimitedBy = []
		self.IsLimitedBy.append(EntityILref.EntityILref())
	def create_OverlapRelease(self):
		self.OverlapRelease =  OverlapRelease.OverlapRelease()

	def __init__(self):
		super().__init__()
		self.___releaseSpeed : tSpeedKmPerHour = None
		"""Release speed in km/h associated with the overlap"""
		self.___overlapSpeed : tSpeedKmPerHour = None
		# @AssociationType Common.tSpeedKmPerHour
		# @AssociationType Common.tSpeedKmPerHour
		# """Maximum speed in the overlap in km/h for other trains than the one using the related route."""
		self.___overlapValidityTime : Duration = 0
		"""The overlap validity time is the time that the train assumes the overlap to be locked. This is the ETCS validity time T_OL."""
		self.___length : tLengthM = None
		# @AssociationType Common.tLengthM
		# """Alternatively to a particular limit the length of the overlap in metres can be given."""
		self.___activeForApproachRoute : EntityILref = None
		"""The reference to the related route using the overlap."""
		self.___relatedToTrackAsset : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """Alternatively to a specific route a reference to a track asset the danger point is related to can be given. This can be a destination signal of a route or any other suitable object."""
		self.___requiresSwitchInPosition : SwitchAndGivenPosition = None
		# @AssociationType Interlocking.SwitchAndGivenPosition*
		# @AssociationMultiplicity 0..*
		# """The reference to any switch in the overlap required to be in a particular position and its position."""
		self.___requiresLevelCrossingInState : LevelCrossingAndGivenState = None
		# @AssociationType Interlocking.LevelCrossingAndGivenState*
		# @AssociationMultiplicity 0..*
		# """The reference to any level crossing in the overlap required to be in a particular state and its state."""
		self.___hasTvdSection : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The reference to any TVD section(s) within the path of the overlap."""
		self.___isLimitedBy : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """References to track assets limiting the overlap. It may be used in conjunction to attribute length."""
		self.___overlapRelease : OverlapRelease = None
		# @AssociationType Interlocking.OverlapRelease
		# @AssociationMultiplicity 0..1
		# """Overlap is set in lockstep with the route. The interlocking releases the overlap when it is safe to presume that an approaching train will not overrun a closed destination signal. When the train occupied the last section (or destination area), an overlap release timer starts running. The timer value is defined by operational rules and the approaching speed. Upon expiry, the interlocking releases the overlap. Overlap is released together with the route or after expiration of the release timer. Overlap is released after a defined time in a timer that starts from a timerTriggerPoint."""
		#self.___unnamed_RouteExit_ : RouteExit = None
		#self.___requiresPointInPosition = []
		#"""# @AssociationMultiplicity 0..*"""
		#self.___requiresAssetInState = []
		#"""# @AssociationMultiplicity 0..*"""