#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.SwitchAndGivenPosition import SwitchAndGivenPosition
from RailML.Interlocking.DerailerAndGivenPosition import DerailerAndGivenPosition
from RailML.Interlocking.CrossingAndGivenPosition import CrossingAndGivenPosition
from RailML.Interlocking.DetectorAndGivenState import DetectorAndGivenState
from RailML.Interlocking.SignalAndGivenAspect import SignalAndGivenAspect
from RailML.Interlocking.SectionAndGivenVacancy import SectionAndGivenVacancy
from RailML.Interlocking.LockAndGivenState import LockAndGivenState
from RailML.Interlocking.LevelCrossingAndGivenState import LevelCrossingAndGivenState
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class RouteRelation(EntityIL):
	"""A route relation states the conditions that must be fulfilled for a given signal to be open. Note that these relations may well be captured in a control table. Therefore, the use is optional."""
	def setRequiredSwitchPosition(self, *aRequiredSwitchPosition : SwitchAndGivenPosition):
		self._requiredSwitchPosition = aRequiredSwitchPosition

	def getRequiredSwitchPosition(self) -> SwitchAndGivenPosition:
		return self._requiredSwitchPosition

	def setRequiredDerailerPosition(self, *aRequiredDerailerPosition : DerailerAndGivenPosition):
		self._requiredDerailerPosition = aRequiredDerailerPosition

	def getRequiredDerailerPosition(self) -> DerailerAndGivenPosition:
		return self._requiredDerailerPosition

	def setRequiredCrossingPosition(self, *aRequiredCrossingPosition : CrossingAndGivenPosition):
		self._requiredCrossingPosition = aRequiredCrossingPosition

	def getRequiredCrossingPosition(self) -> CrossingAndGivenPosition:
		return self._requiredCrossingPosition

	def setRequiredDetectorState(self, *aRequiredDetectorState : DetectorAndGivenState):
		self._requiredDetectorState = aRequiredDetectorState

	def getRequiredDetectorState(self) -> DetectorAndGivenState:
		return self._requiredDetectorState

	def setRequiredSignalAspect(self, *aRequiredSignalAspect : SignalAndGivenAspect):
		self._requiredSignalAspect = aRequiredSignalAspect

	def getRequiredSignalAspect(self) -> SignalAndGivenAspect:
		return self._requiredSignalAspect

	def setRequiredSectionState(self, *aRequiredSectionState : SectionAndGivenVacancy):
		self._requiredSectionState = aRequiredSectionState

	def getRequiredSectionState(self) -> SectionAndGivenVacancy:
		return self._requiredSectionState

	def setRequiredKeyLockState(self, *aRequiredKeyLockState : LockAndGivenState):
		self._requiredKeyLockState = aRequiredKeyLockState

	def getRequiredKeyLockState(self) -> LockAndGivenState:
		return self._requiredKeyLockState

	def setRequiredLevelCrossingState(self, *aRequiredLevelCrossingState : LevelCrossingAndGivenState):
		self._requiredLevelCrossingState = aRequiredLevelCrossingState

	def getRequiredLevelCrossingState(self) -> LevelCrossingAndGivenState:
		return self._requiredLevelCrossingState

	def __init__(self):
		self._requiredSwitchPosition : SwitchAndGivenPosition = None
		# @AssociationType Interlocking.SwitchAndGivenPosition*
		# @AssociationMultiplicity 0..*
		# """References to a particular switch and its required position to fulfil the route relation"""
		self._requiredDerailerPosition : DerailerAndGivenPosition = None
		# @AssociationType Interlocking.DerailerAndGivenPosition*
		# @AssociationMultiplicity 0..*
		# """References to a particular derailer and its required position to fulfil the route relation"""
		self._requiredCrossingPosition : CrossingAndGivenPosition = None
		# @AssociationType Interlocking.CrossingAndGivenPosition*
		# @AssociationMultiplicity 0..*
		# """References to a particular movable crossing and its required position to fulfil the route relation"""
		self._requiredDetectorState : DetectorAndGivenState = None
		# @AssociationType Interlocking.DetectorAndGivenState*
		# @AssociationMultiplicity 0..*
		# """References to a particular detector and its required state to fulfil the route relation"""
		self._requiredSignalAspect : SignalAndGivenAspect = None
		# @AssociationType Interlocking.SignalAndGivenAspect*
		# @AssociationMultiplicity 0..*
		# """References to a particular signal and its required aspect to fulfil the route relation"""
		self._requiredSectionState : SectionAndGivenVacancy = None
		# @AssociationType Interlocking.SectionAndGivenVacancy*
		# @AssociationMultiplicity 0..*
		# """References to a particular TVD section and its required state to fulfil the route relation"""
		self._requiredKeyLockState : LockAndGivenState = None
		# @AssociationType Interlocking.LockAndGivenState*
		# @AssociationMultiplicity 0..*
		# """References to a particular key lock and its required state to fulfil the route relation"""
		self._requiredLevelCrossingState : LevelCrossingAndGivenState = None
		# @AssociationType Interlocking.LevelCrossingAndGivenState*
		# @AssociationMultiplicity 0..*
		# """References to a particular level crossing and its required state to fulfil the route relation"""

