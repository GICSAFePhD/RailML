#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import EntityILref, SwitchInPosition, DerailerInPosition, CrossingInPosition, DetectorInState
from RailML.Interlocking import SignalWithAspect, KeyLockInState, LevelCrossingInState, RestrictedArea
from typing import List

class LocalOperationArea(RestrictedArea.RestrictedArea):
	"""Area used for local shunting movements without routes. Movable elements within the area might be operated from onsite panels. These areas are predefined for parts of a station."""
	


 	def setDeactivationKey(self, *aDeactivationKey : EntityILref):
		self._deactivationKey = aDeactivationKey
	def setSwitchInPosition(self, *aSwitchInPosition : SwitchInPosition):
		self._switchInPosition = aSwitchInPosition
	def setDerailerInPosition(self, *aDerailerInPosition : DerailerInPosition):
		self._derailerInPosition = aDerailerInPosition
	def setCrossingInPosition(self, *aCrossingInPosition : CrossingInPosition):
		self._crossingInPosition = aCrossingInPosition
	def setDetectorInState(self, *aDetectorInState : DetectorInState):
		self._detectorInState = aDetectorInState
	def setSignalWithAspect(self, *aSignalWithAspect : SignalWithAspect):
		self._signalWithAspect = aSignalWithAspect
	def setKeyLockInState(self, *aKeyLockInState : KeyLockInState):
		self._keyLockInState = aKeyLockInState
	def setLevelCrossingInState(self, *aLevelCrossingInState : LevelCrossingInState):
		self._levelCrossingInState = aLevelCrossingInState
	def setReleasedForLocalOperation(self, *aReleasedForLocalOperation : EntityILref):
		self._releasedForLocalOperation = aReleasedForLocalOperation



	def __init__(self):
		self.___deactivationKey : EntityILref = EntityILref.EntityILref()
		"""reference to any device used for deactivate the local operation area after use"""
		self.___switchInPosition : SwitchInPosition = SwitchInPosition.SwitchInPosition()
		# @AssociationType Interlocking.SwitchInPosition*
		# @AssociationMultiplicity 0..*
		# """reference to any switch and its position inside or outside the local operation area required for use and/or protection"""
		self.___derailerInPosition : DerailerInPosition = DerailerInPosition.DerailerInPosition()
		# @AssociationType Interlocking.DerailerInPosition*
		# @AssociationMultiplicity 0..*
		# """reference to any derailer and its position inside or outside the local operation area required for use and/or protection"""
		self.___crossingInPosition : CrossingInPosition = CrossingInPosition.CrossingInPosition()
		# @AssociationType Interlocking.CrossingInPosition*
		# @AssociationMultiplicity 0..*
		# """reference to any movable crossing and its position inside or outside the local operation area required for use and/or protection"""
		self.___detectorInState : DetectorInState = DetectorInState.DetectorInState()
		# @AssociationType Interlocking.DetectorInState*
		# @AssociationMultiplicity 0..*
		# """reference to any detector and its state inside or outside the local operation area required for use"""
		self.___signalWithAspect : SignalWithAspect = SignalWithAspect.SignalWithAspect()
		# @AssociationType Interlocking.SignalWithAspect*
		# @AssociationMultiplicity 0..*
		# """reference to any signal and its aspect inside or outside the local operation area required for use and/or protection"""
		self.___keyLockInState : KeyLockInState = KeyLockInState.KeyLockInState()
		# @AssociationType Interlocking.KeyLockInState*
		# @AssociationMultiplicity 0..*
		# """reference to any key lock and its state inside or outside the local operation area required for use and/or protection"""
		self.___levelCrossingInState : LevelCrossingInState = LevelCrossingInState.LevelCrossingInState()
		# @AssociationType Interlocking.LevelCrossingInState*
		# @AssociationMultiplicity 0..*
		# """reference to any level crossing and its state inside the local operation area required for use"""
		self.___releasedForLocalOperation : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """reference to any element, which is released for local operation, when the local operation area is active"""

