#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import SwitchAndGivenPosition, DerailerAndGivenPosition, CrossingAndGivenPosition
from RailML.Interlocking import DetectorAndGivenState, SignalAndGivenAspect, SectionAndGivenVacancy
from RailML.Interlocking import LockAndGivenState, LevelCrossingAndGivenState, EntityIL
from typing import List

class RouteRelation(EntityIL.EntityIL):
	"""A route relation states the conditions that must be fulfilled for a given signal to be open. Note that these relations may well be captured in a control table. Therefore, the use is optional."""
	@property
	def RequiredSwitchPosition(self) -> SwitchAndGivenPosition:
		return self.___requiredSwitchPosition
	@property
	def RequiredDerailerPosition(self) -> DerailerAndGivenPosition:
		return self.___requiredDerailerPosition
	@property
	def RequiredCrossingPosition(self) -> CrossingAndGivenPosition:
		return self.___requiredCrossingPosition
	@property
	def RequiredDetectorState(self) -> DetectorAndGivenState:
		return self.___requiredDetectorState
	@property
	def RequiredSignalAspect(self) -> SignalAndGivenAspect:
		return self.___requiredSignalAspect
	@property
	def RequiredSectionState(self) -> SectionAndGivenVacancy:
		return self.___requiredSectionState
	@property
	def RequiredKeyLockState(self) -> LockAndGivenState:
		return self.___requiredKeyLockState
	@property
	def RequiredLevelCrossingState(self) -> LevelCrossingAndGivenState:
		return self.___requiredLevelCrossingState

	@RequiredSwitchPosition.setter
	def RequiredSwitchPosition(self, *aRequiredSwitchPosition : SwitchAndGivenPosition):
		self.___requiredSwitchPosition = aRequiredSwitchPosition
	@RequiredDerailerPosition.setter
	def RequiredDerailerPosition(self, *aRequiredDerailerPosition : DerailerAndGivenPosition):
		self.___requiredDerailerPosition = aRequiredDerailerPosition
	@RequiredCrossingPosition.setter
	def RequiredCrossingPosition(self, *aRequiredCrossingPosition : CrossingAndGivenPosition):
		self.___requiredCrossingPosition = aRequiredCrossingPosition
	@RequiredDetectorState.setter
	def RequiredDetectorState(self, *aRequiredDetectorState : DetectorAndGivenState):
		self.___requiredDetectorState = aRequiredDetectorState
	@RequiredSignalAspect.setter
	def RequiredSignalAspect(self, *aRequiredSignalAspect : SignalAndGivenAspect):
		self.___requiredSignalAspect = aRequiredSignalAspect
	@RequiredSectionState.setter
	def RequiredSectionState(self, *aRequiredSectionState : SectionAndGivenVacancy):
		self.___requiredSectionState = aRequiredSectionState
	@RequiredKeyLockState.setter
	def RequiredKeyLockState(self, *aRequiredKeyLockState : LockAndGivenState):
		self.___requiredKeyLockState = aRequiredKeyLockState
	@RequiredLevelCrossingState.setter
	def RequiredLevelCrossingState(self, *aRequiredLevelCrossingState : LevelCrossingAndGivenState):
		self.___requiredLevelCrossingState = aRequiredLevelCrossingState

	def __init__(self):
		self.___requiredSwitchPosition : SwitchAndGivenPosition = SwitchAndGivenPosition.SwitchAndGivenPosition()
		# @AssociationType Interlocking.SwitchAndGivenPosition*
		# @AssociationMultiplicity 0..*
		# """References to a particular switch and its required position to fulfil the route relation"""
		self.___requiredDerailerPosition : DerailerAndGivenPosition = DerailerAndGivenPosition.DerailerAndGivenPosition()
		# @AssociationType Interlocking.DerailerAndGivenPosition*
		# @AssociationMultiplicity 0..*
		# """References to a particular derailer and its required position to fulfil the route relation"""
		self.___requiredCrossingPosition : CrossingAndGivenPosition = CrossingAndGivenPosition.CrossingAndGivenPosition()
		# @AssociationType Interlocking.CrossingAndGivenPosition*
		# @AssociationMultiplicity 0..*
		# """References to a particular movable crossing and its required position to fulfil the route relation"""
		self.___requiredDetectorState : DetectorAndGivenState = DetectorAndGivenState.DetectorAndGivenState()
		# @AssociationType Interlocking.DetectorAndGivenState*
		# @AssociationMultiplicity 0..*
		# """References to a particular detector and its required state to fulfil the route relation"""
		self.___requiredSignalAspect : SignalAndGivenAspect = SignalAndGivenAspect.SignalAndGivenAspect()
		# @AssociationType Interlocking.SignalAndGivenAspect*
		# @AssociationMultiplicity 0..*
		# """References to a particular signal and its required aspect to fulfil the route relation"""
		self.___requiredSectionState : SectionAndGivenVacancy = SectionAndGivenVacancy.SectionAndGivenVacancy()
		# @AssociationType Interlocking.SectionAndGivenVacancy*
		# @AssociationMultiplicity 0..*
		# """References to a particular TVD section and its required state to fulfil the route relation"""
		self.___requiredKeyLockState : LockAndGivenState = LockAndGivenState.LockAndGivenState()
		# @AssociationType Interlocking.LockAndGivenState*
		# @AssociationMultiplicity 0..*
		# """References to a particular key lock and its required state to fulfil the route relation"""
		self.___requiredLevelCrossingState : LevelCrossingAndGivenState = LevelCrossingAndGivenState.LevelCrossingAndGivenState()
		# @AssociationType Interlocking.LevelCrossingAndGivenState*
		# @AssociationMultiplicity 0..*
		# """References to a particular level crossing and its required state to fulfil the route relation"""