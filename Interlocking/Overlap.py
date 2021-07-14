#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tSpeedKmPerHour import tSpeedKmPerHour
from RailML.Common.tLengthM import tLengthM
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.SwitchAndGivenPosition import SwitchAndGivenPosition
from RailML.Interlocking.LevelCrossingAndGivenState import LevelCrossingAndGivenState
from RailML.Interlocking.OverlapRelease import OverlapRelease
from RailML.Interlocking.RouteExit import RouteExit
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class Overlap(EntityIL):
	"""INESS (INtegrated European Signalling System) definition: A defined section of track in advance of a stop signal, or a stopping point in a continuous signalling system, which must be kept clear to avoid the risk of collision should a train inadvertently run past the signal or the stopping point.
	Many IMs require overlap beyond active routes to protect from overshoot. One or more sections beyond the exit signal are locked out from use by other routes. The overlap is delimited by train detectors. Facing switches in the overlap are locked, otherwise, use the swinging overlap. Trailing switches in the overlap may normally not locked. Note that there is no need to explicitly identify the switches in the overlap because they can be derived from the begin and endpoints of the overlap.
	The overlap can be released if the RBC deems that an approaching train is slow enough such that overshoot is unlikely.
	Trains other than the one for which the route-overlap is locked may be attributed a permitted speed in the overlap. If the value is set to 0 it is not possible to set a route through the overlap. Compare this variable with the release speed that applies to the train that is being released beyond the danger point."""
	def setReleaseSpeed(self, aReleaseSpeed : tSpeedKmPerHour):
		self.___releaseSpeed = aReleaseSpeed

	def getReleaseSpeed(self) -> tSpeedKmPerHour:
		return self.___releaseSpeed

	def setOverlapSpeed(self, aOverlapSpeed : tSpeedKmPerHour):
		self.___overlapSpeed = aOverlapSpeed

	def getOverlapSpeed(self) -> tSpeedKmPerHour:
		return self.___overlapSpeed

	def setOverlapValidityTime(self, aOverlapValidityTime : int):	#TODO DEFINED AS duration
		self.___overlapValidityTime = aOverlapValidityTime

	def getOverlapValidityTime(self) -> int:	#TODO DEFINED AS duration
		return self.___overlapValidityTime

	def setLength(self, aLength : tLengthM):
		self.___length = aLength

	def getLength(self) -> tLengthM:
		return self.___length

	def setActiveForApproachRoute(self, aActiveForApproachRoute : EntityILref):
		self._activeForApproachRoute = aActiveForApproachRoute

	def getActiveForApproachRoute(self) -> EntityILref:
		return self._activeForApproachRoute

	def setRelatedToTrackAsset(self, *aRelatedToTrackAsset : EntityILref):
		self._relatedToTrackAsset = aRelatedToTrackAsset

	def getRelatedToTrackAsset(self) -> EntityILref:
		return self._relatedToTrackAsset

	def setRequiresSwitchInPosition(self, *aRequiresSwitchInPosition : SwitchAndGivenPosition):
		self._requiresSwitchInPosition = aRequiresSwitchInPosition

	def getRequiresSwitchInPosition(self) -> SwitchAndGivenPosition:
		return self._requiresSwitchInPosition

	def setRequiresLevelCrossingInState(self, *aRequiresLevelCrossingInState : LevelCrossingAndGivenState):
		self._requiresLevelCrossingInState = aRequiresLevelCrossingInState

	def getRequiresLevelCrossingInState(self) -> LevelCrossingAndGivenState:
		return self._requiresLevelCrossingInState

	def setHasTvdSection(self, *aHasTvdSection : EntityILref):
		self._hasTvdSection = aHasTvdSection

	def getHasTvdSection(self) -> EntityILref:
		return self._hasTvdSection

	def setIsLimitedBy(self, *aIsLimitedBy : EntityILref):
		self._isLimitedBy = aIsLimitedBy

	def getIsLimitedBy(self) -> EntityILref:
		return self._isLimitedBy

	def setOverlapRelease(self, aOverlapRelease : OverlapRelease):
		self._overlapRelease = aOverlapRelease

	def getOverlapRelease(self) -> OverlapRelease:
		return self._overlapRelease

	def __init__(self):
		self.___releaseSpeed : tSpeedKmPerHour = None
		"""Release speed in km/h associated with the overlap"""
		self.___overlapSpeed : tSpeedKmPerHour = None
		# @AssociationType Common.tSpeedKmPerHour
		# @AssociationType Common.tSpeedKmPerHour
		# """Maximum speed in the overlap in km/h for other trains than the one using the related route."""
		self.___overlapValidityTime : int = None	#TODO DEFINED AS duration
		"""The overlap validity time is the time that the train assumes the overlap to be locked. This is the ETCS validity time T_OL."""
		self.___length : tLengthM = None
		# @AssociationType Common.tLengthM
		# """Alternatively to a particular limit the length of the overlap in metres can be given."""
		self._activeForApproachRoute : EntityILref = None
		"""The reference to the related route using the overlap."""
		self._relatedToTrackAsset : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """Alternatively to a specific route a reference to a track asset the danger point is related to can be given. This can be a destination signal of a route or any other suitable object."""
		self._requiresSwitchInPosition : SwitchAndGivenPosition = None
		# @AssociationType Interlocking.SwitchAndGivenPosition*
		# @AssociationMultiplicity 0..*
		# """The reference to any switch in the overlap required to be in a particular position and its position."""
		self._requiresLevelCrossingInState : LevelCrossingAndGivenState = None
		# @AssociationType Interlocking.LevelCrossingAndGivenState*
		# @AssociationMultiplicity 0..*
		# """The reference to any level crossing in the overlap required to be in a particular state and its state."""
		self._hasTvdSection : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The reference to any TVD section(s) within the path of the overlap."""
		self._isLimitedBy : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """References to track assets limiting the overlap. It may be used in conjunction to attribute length."""
		self._overlapRelease : OverlapRelease = None
		# @AssociationType Interlocking.OverlapRelease
		# @AssociationMultiplicity 0..1
		# """Overlap is set in lockstep with the route. The interlocking releases the overlap when it is safe to presume that an approaching train will not overrun a closed destination signal. When the train occupied the last section (or destination area), an overlap release timer starts running. The timer value is defined by operational rules and the approaching speed. Upon expiry, the interlocking releases the overlap. Overlap is released together with the route or after expiration of the release timer. Overlap is released after a defined time in a timer that starts from a timerTriggerPoint."""
		self._unnamed_RouteExit_ : RouteExit = None
		self._requiresPointInPosition = []
		"""# @AssociationMultiplicity 0..*"""
		self._requiresAssetInState = []
		"""# @AssociationMultiplicity 0..*"""

