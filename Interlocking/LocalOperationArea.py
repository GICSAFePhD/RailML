#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import EntityILref
from Interlocking import SwitchInPosition
from Interlocking import DerailerInPosition
from Interlocking import CrossingInPosition
from Interlocking import DetectorInState
from Interlocking import SignalWithAspect
from Interlocking import KeyLockInState
from Interlocking import LevelCrossingInState
from Interlocking import RestrictedArea
from typing import List

class LocalOperationArea(RestrictedArea):
	"""Area used for local shunting movements without routes. Movable elements within the area might be operated from onsite panels. These areas are predefined for parts of a station."""
	def setDeactivationKey(self, *aDeactivationKey : EntityILref*):
		self._deactivationKey = aDeactivationKey

	def getDeactivationKey(self) -> EntityILref*:
		return self._deactivationKey

	def setSwitchInPosition(self, *aSwitchInPosition : SwitchInPosition*):
		self._switchInPosition = aSwitchInPosition

	def getSwitchInPosition(self) -> SwitchInPosition*:
		return self._switchInPosition

	def setDerailerInPosition(self, *aDerailerInPosition : DerailerInPosition*):
		self._derailerInPosition = aDerailerInPosition

	def getDerailerInPosition(self) -> DerailerInPosition*:
		return self._derailerInPosition

	def setCrossingInPosition(self, *aCrossingInPosition : CrossingInPosition*):
		self._crossingInPosition = aCrossingInPosition

	def getCrossingInPosition(self) -> CrossingInPosition*:
		return self._crossingInPosition

	def setDetectorInState(self, *aDetectorInState : DetectorInState*):
		self._detectorInState = aDetectorInState

	def getDetectorInState(self) -> DetectorInState*:
		return self._detectorInState

	def setSignalWithAspect(self, *aSignalWithAspect : SignalWithAspect*):
		self._signalWithAspect = aSignalWithAspect

	def getSignalWithAspect(self) -> SignalWithAspect*:
		return self._signalWithAspect

	def setKeyLockInState(self, *aKeyLockInState : KeyLockInState*):
		self._keyLockInState = aKeyLockInState

	def getKeyLockInState(self) -> KeyLockInState*:
		return self._keyLockInState

	def setLevelCrossingInState(self, *aLevelCrossingInState : LevelCrossingInState*):
		self._levelCrossingInState = aLevelCrossingInState

	def getLevelCrossingInState(self) -> LevelCrossingInState*:
		return self._levelCrossingInState

	def setReleasedForLocalOperation(self, *aReleasedForLocalOperation : EntityILref*):
		self._releasedForLocalOperation = aReleasedForLocalOperation

	def getReleasedForLocalOperation(self) -> EntityILref*:
		return self._releasedForLocalOperation

	def __init__(self):
		self._deactivationKey : EntityILref = None
		"""reference to any device used for deactivate the local operation area after use"""
		self._switchInPosition : SwitchInPosition = None
		# @AssociationType Interlocking.SwitchInPosition*
		# @AssociationMultiplicity 0..*
		# """reference to any switch and its position inside or outside the local operation area required for use and/or protection"""
		self._derailerInPosition : DerailerInPosition = None
		# @AssociationType Interlocking.DerailerInPosition*
		# @AssociationMultiplicity 0..*
		# """reference to any derailer and its position inside or outside the local operation area required for use and/or protection"""
		self._crossingInPosition : CrossingInPosition = None
		# @AssociationType Interlocking.CrossingInPosition*
		# @AssociationMultiplicity 0..*
		# """reference to any movable crossing and its position inside or outside the local operation area required for use and/or protection"""
		self._detectorInState : DetectorInState = None
		# @AssociationType Interlocking.DetectorInState*
		# @AssociationMultiplicity 0..*
		# """reference to any detector and its state inside or outside the local operation area required for use"""
		self._signalWithAspect : SignalWithAspect = None
		# @AssociationType Interlocking.SignalWithAspect*
		# @AssociationMultiplicity 0..*
		# """reference to any signal and its aspect inside or outside the local operation area required for use and/or protection"""
		self._keyLockInState : KeyLockInState = None
		# @AssociationType Interlocking.KeyLockInState*
		# @AssociationMultiplicity 0..*
		# """reference to any key lock and its state inside or outside the local operation area required for use and/or protection"""
		self._levelCrossingInState : LevelCrossingInState = None
		# @AssociationType Interlocking.LevelCrossingInState*
		# @AssociationMultiplicity 0..*
		# """reference to any level crossing and its state inside the local operation area required for use"""
		self._releasedForLocalOperation : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """reference to any element, which is released for local operation, when the local operation area is active"""

