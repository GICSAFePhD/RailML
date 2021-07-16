#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tLengthM import tLengthM
from RailML.Common.tSpeedKmPerHour import tSpeedKmPerHour
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.RouteExit import RouteExit
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class DangerPoint(EntityIL):
	"""The danger point defines the position beyond the exit signal up to where a train is likely to be safe.
	Designed for ETCS modelling."""
	def setDistance(self, aDistance : tLengthM):
		self.___distance = aDistance

	def getDistance(self) -> tLengthM:
		return self.___distance

	def setReleaseSpeed(self, aReleaseSpeed : tSpeedKmPerHour):
		self.___releaseSpeed = aReleaseSpeed

	def getReleaseSpeed(self) -> tSpeedKmPerHour:
		return self.___releaseSpeed

	def setLastSupervisedSectionBeforeDP(self, aLastSupervisedSectionBeforeDP : EntityILref):
		self._lastSupervisedSectionBeforeDP = aLastSupervisedSectionBeforeDP

	def getLastSupervisedSectionBeforeDP(self) -> EntityILref:
		return self._lastSupervisedSectionBeforeDP

	def setSituatedAtTrackAsset(self, aSituatedAtTrackAsset : EntityILref):
		self._situatedAtTrackAsset = aSituatedAtTrackAsset

	def getSituatedAtTrackAsset(self) -> EntityILref:
		return self._situatedAtTrackAsset

	def __init__(self):
		self.___distance : tLengthM = None
		# @AssociationType Common.tLengthM
		# """Distance in metres from exit signal to danger point. Optional because one may also derive this distance from the track asset where the danger point is situated."""
		self.___releaseSpeed : tSpeedKmPerHour = None
		# @AssociationType Common.tSpeedKmPerHour
		# """Release speed in km/h associated with the danger point."""
		self._lastSupervisedSectionBeforeDP : EntityILref = None
		"""This is the reference to last TVD section which is completely before the danger point. It is used when the danger point is situated at the end of a TVD section."""
		self._situatedAtTrackAsset : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# """This is the reference to the track asset the danger point is located. It is used when the danger point is situated in the middle of a TVD section or beyond any TVD section in case of not supervised tracks."""
		self._unnamed_RouteExit_ : RouteExit = None

