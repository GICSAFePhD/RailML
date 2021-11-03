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
	def RequiredSwitchPosition(self, aRequiredSwitchPosition : SwitchAndGivenPosition):	# TODO *aRequiredSwitchPosition
		self.___requiredSwitchPosition = aRequiredSwitchPosition
	@RequiredDerailerPosition.setter
	def RequiredDerailerPosition(self, aRequiredDerailerPosition : DerailerAndGivenPosition):	# TODO *aRequiredDerailerPosition
		self.___requiredDerailerPosition = aRequiredDerailerPosition
	@RequiredCrossingPosition.setter
	def RequiredCrossingPosition(self, aRequiredCrossingPosition : CrossingAndGivenPosition):	# TODO *aRequiredCrossingPosition
		self.___requiredCrossingPosition = aRequiredCrossingPosition
	@RequiredDetectorState.setter
	def RequiredDetectorState(self, aRequiredDetectorState : DetectorAndGivenState):	# TODO *aRequiredDetectorState
		self.___requiredDetectorState = aRequiredDetectorState
	@RequiredSignalAspect.setter
	def RequiredSignalAspect(self, aRequiredSignalAspect : SignalAndGivenAspect):	# TODO *aRequiredSignalAspect
		self.___requiredSignalAspect = aRequiredSignalAspect
	@RequiredSectionState.setter
	def RequiredSectionState(self, aRequiredSectionState : SectionAndGivenVacancy):	# TODO *aRequiredSectionState
		self.___requiredSectionState = aRequiredSectionState
	@RequiredKeyLockState.setter
	def RequiredKeyLockState(self, aRequiredKeyLockState : LockAndGivenState):	# TODO *aRequiredKeyLockState
		self.___requiredKeyLockState = aRequiredKeyLockState
	@RequiredLevelCrossingState.setter
	def RequiredLevelCrossingState(self, aRequiredLevelCrossingState : LevelCrossingAndGivenState):	# TODO *aRequiredLevelCrossingState
		self.___requiredLevelCrossingState = aRequiredLevelCrossingState

	def create_RequiredSwitchPosition(self):
		if self.RequiredSwitchPosition == None:
			self.RequiredSwitchPosition = []
		self.RequiredSwitchPosition.append(SwitchAndGivenPosition.SwitchAndGivenPosition())
	def create_RequiredDerailerPosition(self):
		if self.RequiredDerailerPosition == None:
			self.RequiredDerailerPosition = []
		self.RequiredDerailerPosition.append(DerailerAndGivenPosition.DerailerAndGivenPosition())
	def create_RequiredCrossingPosition(self):
		if self.RequiredCrossingPosition == None:
			self.RequiredCrossingPosition = []
		self.RequiredCrossingPosition.append(CrossingAndGivenPosition.CrossingAndGivenPosition())
	def create_RequiredDetectorState(self):
		if self.RequiredDetectorState == None:
			self.RequiredDetectorState = []
		self.RequiredDetectorState.append(DetectorAndGivenState.DetectorAndGivenState())
	def create_RequiredSignalAspect(self):
		if self.RequiredSignalAspect == None:
			self.RequiredSignalAspect = []
		self.RequiredSignalAspect.append(SignalAndGivenAspect.SignalAndGivenAspect())
	def create_RequiredSectionState(self):
		if self.RequiredSectionState == None:
			self.RequiredSectionState = []
		self.RequiredSectionState.append(SectionAndGivenVacancy.SectionAndGivenVacancy())
	def create_RequiredKeyLockState(self):
		if self.RequiredKeyLockState == None:
			self.RequiredKeyLockState = []
		self.RequiredKeyLockState.append(LockAndGivenState.LockAndGivenState())
	def create_RequiredLevelCrossingState(self):
		if self.RequiredLevelCrossingState == None:
			self.RequiredLevelCrossingState = []
		self.RequiredLevelCrossingState.append(LevelCrossingAndGivenState.LevelCrossingAndGivenState())

	def __init__(self):
		super().__init__()
		self.___requiredSwitchPosition : SwitchAndGivenPosition = None
		# @AssociationType Interlocking.SwitchAndGivenPosition*
		# @AssociationMultiplicity 0..*
		# """References to a particular switch and its required position to fulfil the route relation"""
		self.___requiredDerailerPosition : DerailerAndGivenPosition = None
		# @AssociationType Interlocking.DerailerAndGivenPosition*
		# @AssociationMultiplicity 0..*
		# """References to a particular derailer and its required position to fulfil the route relation"""
		self.___requiredCrossingPosition : CrossingAndGivenPosition = None
		# @AssociationType Interlocking.CrossingAndGivenPosition*
		# @AssociationMultiplicity 0..*
		# """References to a particular movable crossing and its required position to fulfil the route relation"""
		self.___requiredDetectorState : DetectorAndGivenState = None
		# @AssociationType Interlocking.DetectorAndGivenState*
		# @AssociationMultiplicity 0..*
		# """References to a particular detector and its required state to fulfil the route relation"""
		self.___requiredSignalAspect : SignalAndGivenAspect = None
		# @AssociationType Interlocking.SignalAndGivenAspect*
		# @AssociationMultiplicity 0..*
		# """References to a particular signal and its required aspect to fulfil the route relation"""
		self.___requiredSectionState : SectionAndGivenVacancy = None
		# @AssociationType Interlocking.SectionAndGivenVacancy*
		# @AssociationMultiplicity 0..*
		# """References to a particular TVD section and its required state to fulfil the route relation"""
		self.___requiredKeyLockState : LockAndGivenState = None
		# @AssociationType Interlocking.LockAndGivenState*
		# @AssociationMultiplicity 0..*
		# """References to a particular key lock and its required state to fulfil the route relation"""
		self.___requiredLevelCrossingState : LevelCrossingAndGivenState = None
		# @AssociationType Interlocking.LevelCrossingAndGivenState*
		# @AssociationMultiplicity 0..*
		# """References to a particular level crossing and its required state to fulfil the route relation"""