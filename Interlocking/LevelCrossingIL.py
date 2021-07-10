#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import tLevelCrossingState
from Common import tSpeedKmPerHour
from Interlocking import EntityILref
from Interlocking import LevelCrossingDeactivator
from Interlocking import ActivationCondition
from Interlocking import TrackAsset
from typing import List

class LevelCrossingIL(TrackAsset):
	"""A level crossing (LX) is activated, i.e. requested to close for road traffic, upon train approach. This happens when the train crosses a detection point, i.e. an insulated track joint, axle counter or treadle. These approach detectors are commonly referred to as Approach Starting (AS)."""
	def setPreferredPosition(self, aPreferredPosition : tLevelCrossingState):
		self.___preferredPosition = aPreferredPosition

	def getPreferredPosition(self) -> tLevelCrossingState:
		return self.___preferredPosition

	def setUnprotectedSpeed(self, aUnprotectedSpeed : tSpeedKmPerHour):
		self.___unprotectedSpeed = aUnprotectedSpeed

	def getUnprotectedSpeed(self) -> tSpeedKmPerHour:
		return self.___unprotectedSpeed

	def setTypicalTimeToClose(self, aTypicalTimeToClose : duration):
		self.___typicalTimeToClose = aTypicalTimeToClose

	def getTypicalTimeToClose(self) -> duration:
		return self.___typicalTimeToClose

	def setConstantWarningTime(self, aConstantWarningTime : duration):
		self.___constantWarningTime = aConstantWarningTime

	def getConstantWarningTime(self) -> duration:
		return self.___constantWarningTime

	def setMinimumOpenTime(self, aMinimumOpenTime : duration):
		self.___minimumOpenTime = aMinimumOpenTime

	def getMinimumOpenTime(self) -> duration:
		return self.___minimumOpenTime

	def setMaximumClosedTime(self, aMaximumClosedTime : duration):
		self.___maximumClosedTime = aMaximumClosedTime

	def getMaximumClosedTime(self) -> duration:
		return self.___maximumClosedTime

	def setRequiresStopBeforeUnprotectedLevelCrossing(self, aRequiresStopBeforeUnprotectedLevelCrossing : long):
		self.___requiresStopBeforeUnprotectedLevelCrossing = aRequiresStopBeforeUnprotectedLevelCrossing

	def getRequiresStopBeforeUnprotectedLevelCrossing(self) -> long:
		return self.___requiresStopBeforeUnprotectedLevelCrossing

	def setHasInterface(self, aHasInterface : EntityILref):
		self._hasInterface = aHasInterface

	def getHasInterface(self) -> EntityILref:
		return self._hasInterface

	def setIsLevelCrossingType(self, aIsLevelCrossingType : EntityILref):
		self._isLevelCrossingType = aIsLevelCrossingType

	def getIsLevelCrossingType(self) -> EntityILref:
		return self._isLevelCrossingType

	def setRefersTo(self, *aRefersTo : EntityILref*):
		self._refersTo = aRefersTo

	def getRefersTo(self) -> EntityILref*:
		return self._refersTo

	def setDeactivatedBy(self, *aDeactivatedBy : LevelCrossingDeactivator*):
		self._deactivatedBy = aDeactivatedBy

	def getDeactivatedBy(self) -> LevelCrossingDeactivator*:
		return self._deactivatedBy

	def setActivationCondition(self, *aActivationCondition : ActivationCondition*):
		self._activationCondition = aActivationCondition

	def getActivationCondition(self) -> ActivationCondition*:
		return self._activationCondition

	def setHasTvdSection(self, aHasTvdSection : EntityILref):
		self._hasTvdSection = aHasTvdSection

	def getHasTvdSection(self) -> EntityILref:
		return self._hasTvdSection

	def __init__(self):
		self.___preferredPosition : tLevelCrossingState = None
		# @AssociationType Interlocking.tLevelCrossingState
		# """This is the state of level crossing under normal conditions, i.e. when not in use. For most level crossings this would be the open state."""
		self.___unprotectedSpeed : tSpeedKmPerHour = None
		# @AssociationType Common.tSpeedKmPerHour
		# """Speed in km/h at which the level crossing can be passed when it is not protected (V_LX)"""
		self.___typicalTimeToClose : duration = None
		"""Average time between the time a train detector notes an approaching train and the moment the level crossing is closed to road traffic, i.e. the moment that the interlocking can lock a route across the level crossing. This equates to the time it takes to close the barrier (if present). Should be set to 0 if no barrier is configured. Useful for simulation."""
		self.___constantWarningTime : duration = None
		"""A level crossing must cause as little as possible hindering to train as well as road traffic. Therefore, the level crossing must close as late as safely possible. The optimal delay, known as constant warning time, between activation and closing is possible when the train speed and position are known."""
		self.___minimumOpenTime : duration = None
		"""This is the time the level crossing has to be open before it is allowed to close again. This is to ensure a certain capacity for the crossing road traffic."""
		self.___maximumClosedTime : duration = None
		"""This is the time span after a message to the operator is triggered because a level crossing being closed for too long time can be considered as unsafe. In such cases the road drivers and pedestrians might try to cross the railway line illegally."""
		self.___requiresStopBeforeUnprotectedLevelCrossing : long = None
		"""Flag to define whether any train needs to stop in front of the level crossing in case it is unprotected. Only afterwards it can proceed according the value in speedRestriction."""
		self._hasInterface : EntityILref = None
		"""Reference to physical description of level crossing interface with list of commands to the field and notifications from the field"""
		self._isLevelCrossingType : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """Reference to the basic type of level crossing. It refers to a basic configuration of a level crossing for this IM."""
		self._refersTo : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The reference to the physical level crossing in infrastructure."""
		self._deactivatedBy : LevelCrossingDeactivator = None
		# @AssociationType Interlocking.LevelCrossingDeactivator*
		# @AssociationMultiplicity 0..*
		# """The description of deactivation conditions for this level crossing."""
		self._activationCondition : ActivationCondition = None
		# @AssociationType Interlocking.ActivationCondition*
		# @AssociationMultiplicity 0..*
		# """Description of the possible activation conditions of this level crossing."""
		self._hasTvdSection : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# """The reference to the TVD section(s) directly at the level crossing"""

