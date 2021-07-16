#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.SwitchInPosition import SwitchInPosition
from RailML.Interlocking.DerailerInPosition import DerailerInPosition
from RailML.Interlocking.CrossingInPosition import CrossingInPosition
from RailML.Interlocking.DetectorInState import DetectorInState
from RailML.Interlocking.SignalWithAspect import SignalWithAspect
from RailML.Interlocking.KeyLockInState import KeyLockInState
from RailML.Interlocking.LevelCrossingInState import LevelCrossingInState
from RailML.Interlocking.RestrictedArea import RestrictedArea
from typing import List

class WorkZone(RestrictedArea):
	"""A set of track assets that track workers or the signalman can set apart from the main line. When taken, it is impossible to call regular routes into this work zone."""
	def setActivationLock(self, *aActivationLock : EntityILref):
		self._activationLock = aActivationLock

	def getActivationLock(self) -> EntityILref:
		return self._activationLock

	def setSwitchInPosition(self, *aSwitchInPosition : SwitchInPosition):
		self._switchInPosition = aSwitchInPosition

	def getSwitchInPosition(self) -> SwitchInPosition:
		return self._switchInPosition

	def setDerailerInPosition(self, *aDerailerInPosition : DerailerInPosition):
		self._derailerInPosition = aDerailerInPosition

	def getDerailerInPosition(self) -> DerailerInPosition:
		return self._derailerInPosition

	def setCrossingInPosition(self, *aCrossingInPosition : CrossingInPosition):
		self._crossingInPosition = aCrossingInPosition

	def getCrossingInPosition(self) -> CrossingInPosition:
		return self._crossingInPosition

	def setDetectorInState(self, *aDetectorInState : DetectorInState):
		self._detectorInState = aDetectorInState

	def getDetectorInState(self) -> DetectorInState:
		return self._detectorInState

	def setSignalWithAspect(self, *aSignalWithAspect : SignalWithAspect):
		self._signalWithAspect = aSignalWithAspect

	def getSignalWithAspect(self) -> SignalWithAspect:
		return self._signalWithAspect

	def setKeyLockInState(self, *aKeyLockInState : KeyLockInState):
		self._keyLockInState = aKeyLockInState

	def getKeyLockInState(self) -> KeyLockInState:
		return self._keyLockInState

	def setLevelCrossingInState(self, *aLevelCrossingInState : LevelCrossingInState):
		self._levelCrossingInState = aLevelCrossingInState

	def getLevelCrossingInState(self) -> LevelCrossingInState:
		return self._levelCrossingInState

	def setReleasedForLocalOperation(self, *aReleasedForLocalOperation : EntityILref):
		self._releasedForLocalOperation = aReleasedForLocalOperation

	def getReleasedForLocalOperation(self) -> EntityILref:
		return self._releasedForLocalOperation

	def __init__(self):
		self._activationLock : EntityILref = None
		"""reference to any locking device used for activation of the work zone"""
		self._switchInPosition : SwitchInPosition = None
		# @AssociationType Interlocking.SwitchInPosition*
		# @AssociationMultiplicity 0..*
		# """reference to any switch and its position inside or outside the work zone required for use and/or protection"""
		self._derailerInPosition : DerailerInPosition = None
		# @AssociationType Interlocking.DerailerInPosition*
		# @AssociationMultiplicity 0..*
		# """reference to any derailer and its position inside or outside the work zone required for use and/or protection"""
		self._crossingInPosition : CrossingInPosition = None
		# @AssociationType Interlocking.CrossingInPosition*
		# @AssociationMultiplicity 0..*
		# """reference to any movable crossing and its position inside or outside the work zone required for use and/or protection"""
		self._detectorInState : DetectorInState = None
		# @AssociationType Interlocking.DetectorInState*
		# @AssociationMultiplicity 0..*
		# """reference to any detector and its state inside or outside the work zone required for use"""
		self._signalWithAspect : SignalWithAspect = None
		# @AssociationType Interlocking.SignalWithAspect*
		# @AssociationMultiplicity 0..*
		# """reference to any signal and its aspect inside or outside the work zone required for use and/or protection"""
		self._keyLockInState : KeyLockInState = None
		# @AssociationType Interlocking.KeyLockInState*
		# @AssociationMultiplicity 0..*
		# """reference to any key log and its state inside or outside the work zone required for use and/or protection"""
		self._levelCrossingInState : LevelCrossingInState = None
		# @AssociationType Interlocking.LevelCrossingInState*
		# @AssociationMultiplicity 0..*
		# """reference to any level crossing and its state inside the work zone required for use"""
		self._releasedForLocalOperation : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """reference to any element, which is released for local operation, when the work zone is active"""

