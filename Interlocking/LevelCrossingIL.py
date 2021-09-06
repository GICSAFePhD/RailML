#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tSpeedKmPerHour
from RailML.Interlocking import tLevelCrossingState, EntityILref, LevelCrossingDeactivator, ActivationCondition, TrackAsset
from typing import List, NewType
Duration = NewType("Duration", int)
Long = NewType("Long", int)

class LevelCrossingIL(TrackAsset.TrackAsset):
	"""A level crossing (LX) is activated, i.e. requested to close for road traffic, upon train approach. This happens when the train crosses a detection point, i.e. an insulated track joint, axle counter or treadle. These approach detectors are commonly referred to as Approach Starting (AS)."""
	@property
	def PreferredPosition(self) -> tLevelCrossingState:
		return self.___preferredPosition
	@property
	def UnprotectedSpeed(self) -> tSpeedKmPerHour:
		return self.___unprotectedSpeed
	@property
	def TypicalTimeToClose(self) -> Duration:
		return self.___typicalTimeToClose
	@property
	def ConstantWarningTime(self) -> Duration:
		return self.___constantWarningTime
	@property
	def MinimumOpenTime(self) -> Duration:
		return self.___minimumOpenTime
	@property
	def MaximumClosedTime(self) -> Duration:
		return self.___maximumClosedTime
	@property
	def RequiresStopBeforeUnprotectedLevelCrossing(self) -> Long:
		return self.___requiresStopBeforeUnprotectedLevelCrossing
	@property
	def HasInterface(self) -> EntityILref:
		return self.___hasInterface
	@property
	def IsLevelCrossingType(self) -> EntityILref:
		return self.___isLevelCrossingType
	@property
	def RefersTo(self) -> EntityILref:
		return self.___refersTo
	@property
	def DeactivatedBy(self) -> LevelCrossingDeactivator:
		return self.___deactivatedBy
	@property
	def ActivationCondition(self) -> ActivationCondition:
		return self.___activationCondition
	@property
	def HasTvdSection(self) -> EntityILref:
		return self.___hasTvdSection

	@PreferredPosition.setter
	def PreferredPosition(self, aPreferredPosition : tLevelCrossingState):
		self.___preferredPosition = aPreferredPosition
	@UnprotectedSpeed.setter
	def UnprotectedSpeed(self, aUnprotectedSpeed : tSpeedKmPerHour):
		self.___unprotectedSpeed = aUnprotectedSpeed
	@TypicalTimeToClose.setter
	def TypicalTimeToClose(self, aTypicalTimeToClose : Duration):
		self.___typicalTimeToClose = aTypicalTimeToClose
	@ConstantWarningTime.setter
	def ConstantWarningTime(self, aConstantWarningTime : Duration):
		self.___constantWarningTime = aConstantWarningTime
	@MinimumOpenTime.setter
	def MinimumOpenTime(self, aMinimumOpenTime : Duration):
		self.___minimumOpenTime = aMinimumOpenTime
	@MaximumClosedTime.setter
	def MaximumClosedTime(self, aMaximumClosedTime : Duration):
		self.___maximumClosedTime = aMaximumClosedTime
	@RequiresStopBeforeUnprotectedLevelCrossing.setter
	def RequiresStopBeforeUnprotectedLevelCrossing(self, aRequiresStopBeforeUnprotectedLevelCrossing : Long):
		self.___requiresStopBeforeUnprotectedLevelCrossing = aRequiresStopBeforeUnprotectedLevelCrossing
	@HasInterface.setter
	def HasInterface(self, aHasInterface : EntityILref):
		self.___hasInterface = aHasInterface
	@IsLevelCrossingType.setter
	def IsLevelCrossingType(self, aIsLevelCrossingType : EntityILref):
		self.___isLevelCrossingType = aIsLevelCrossingType
	@RefersTo.setter
	def RefersTo(self, *aRefersTo : EntityILref):
		self.___refersTo = aRefersTo
	@DeactivatedBy.setter
	def DeactivatedBy(self, *aDeactivatedBy : LevelCrossingDeactivator):
		self.___deactivatedBy = aDeactivatedBy
	@ActivationCondition.setter
	def ActivationCondition(self, *aActivationCondition : ActivationCondition):
		self.___activationCondition = aActivationCondition
	@HasTvdSection.setter
	def HasTvdSection(self, aHasTvdSection : EntityILref):
		self.___hasTvdSection = aHasTvdSection

	def create_HasInterface(self):
		self.HasInterface = EntityILref.EntityILref()
	def create_IsLevelCrossingType(self):
		self.IsLevelCrossingType = EntityILref.EntityILref()
	def create_RefersTo(self):
		self.RefersTo = EntityILref.EntityILref()
	def create_DeactivatedBy(self):
		if self.DeactivatedBy == None:
			self.DeactivatedBy = []
		self.DeactivatedBy.append(EntityILref.EntityILref())
	def create_ActivationCondition(self):
		if self.ActivationCondition == None:
			self.ActivationCondition = []
		self.ActivationCondition.append(EntityILref.EntityILref())
	def create_HasTvdSection(self):
		if self.HasTvdSection == None:
			self.HasTvdSection = []
		self.HasTvdSection.append(EntityILref.EntityILref())

	def __init__(self):
		super().__init__()
		self.___preferredPosition : tLevelCrossingState = None
		# @AssociationType Interlocking.tLevelCrossingState
		# """This is the state of level crossing under normal conditions, i.e. when not in use. For most level crossings this would be the open state."""
		self.___unprotectedSpeed : tSpeedKmPerHour = None
		# @AssociationType Common.tSpeedKmPerHour
		# """Speed in km/h at which the level crossing can be passed when it is not protected (V_LX)"""
		self.___typicalTimeToClose : Duration = 0
		"""Average time between the time a train detector notes an approaching train and the moment the level crossing is closed to road traffic, i.e. the moment that the interlocking can lock a route across the level crossing. This equates to the time it takes to close the barrier (if present). Should be set to 0 if no barrier is configured. Useful for simulation."""
		self.___constantWarningTime : Duration = 0
		"""A level crossing must cause as little as possible hindering to train as well as road traffic. Therefore, the level crossing must close as late as safely possible. The optimal delay, known as constant warning time, between activation and closing is possible when the train speed and position are known."""
		self.___minimumOpenTime : Duration = 0
		"""This is the time the level crossing has to be open before it is allowed to close again. This is to ensure a certain capacity for the crossing road traffic."""
		self.___maximumClosedTime : Duration = 0
		"""This is the time span after a message to the operator is triggered because a level crossing being closed for too long time can be considered as unsafe. In such cases the road drivers and pedestrians might try to cross the railway line illegally."""
		self.___requiresStopBeforeUnprotectedLevelCrossing : Long = 0
		"""Flag to define whether any train needs to stop in front of the level crossing in case it is unprotected. Only afterwards it can proceed according the value in speedRestriction."""
		self.___hasInterface : EntityILref = None
		"""Reference to physical description of level crossing interface with list of commands to the field and notifications from the field"""
		self.___isLevelCrossingType : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """Reference to the basic type of level crossing. It refers to a basic configuration of a level crossing for this IM."""
		self.___refersTo : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The reference to the physical level crossing in infrastructure."""
		self.___deactivatedBy : LevelCrossingDeactivator = None
		# @AssociationType Interlocking.LevelCrossingDeactivator*
		# @AssociationMultiplicity 0..*
		# """The description of deactivation conditions for this level crossing."""
		self.___activationCondition : ActivationCondition = None
		# @AssociationType Interlocking.ActivationCondition*
		# @AssociationMultiplicity 0..*
		# """Description of the possible activation conditions of this level crossing."""
		self.___hasTvdSection : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# """The reference to the TVD section(s) directly at the level crossing"""