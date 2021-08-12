#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import EntityILref, SwitchInPosition, DerailerInPosition
from RailML.Interlocking import CrossingInPosition, DetectorInState, SignalWithAspect
from RailML.Interlocking import KeyLockInState, LevelCrossingInState, RestrictedArea
from typing import List

class WorkZone(RestrictedArea.RestrictedArea):
	"""A set of track assets that track workers or the signalman can set apart from the main line. When taken, it is impossible to call regular routes into this work zone."""
	@property
	def ActivationLock(self) -> EntityILref:
		return self.___activationLock
	@property
	def SwitchInPosition(self) -> SwitchInPosition:
		return self.___switchInPosition
	@property
	def DerailerInPosition(self) -> DerailerInPosition:
		return self.___derailerInPosition
	@property
	def CrossingInPosition(self) -> CrossingInPosition:
		return self.___crossingInPosition
	@property
	def DetectorInState(self) -> DetectorInState:
		return self.___detectorInState
	@property
	def SignalWithAspect(self) -> SignalWithAspect:
		return self.___signalWithAspect
	@property
	def KeyLockInState(self) -> KeyLockInState:
		return self.___keyLockInState
	@property
	def LevelCrossingInState(self) -> LevelCrossingInState:
		return self.___levelCrossingInState
	@property
	def ReleasedForLocalOperation(self) -> EntityILref:
		return self.___releasedForLocalOperation

	@ActivationLock.setter
	def ActivationLock(self, *aActivationLock : EntityILref):
		self.___activationLock = aActivationLock
	@SwitchInPosition.setter
	def SwitchInPosition(self, *aSwitchInPosition : SwitchInPosition):
		self.___switchInPosition = aSwitchInPosition
	@DerailerInPosition.setter
	def DerailerInPosition(self, *aDerailerInPosition : DerailerInPosition):
		self.___derailerInPosition = aDerailerInPosition
	@CrossingInPosition.setter
	def CrossingInPosition(self, *aCrossingInPosition : CrossingInPosition):
		self.___crossingInPosition = aCrossingInPosition
	@DetectorInState.setter
	def DetectorInState(self, *aDetectorInState : DetectorInState):
		self.___detectorInState = aDetectorInState
	@SignalWithAspect.setter
	def SignalWithAspect(self, *aSignalWithAspect : SignalWithAspect):
		self.___signalWithAspect = aSignalWithAspect
	@KeyLockInState.setter
	def KeyLockInState(self, *aKeyLockInState : KeyLockInState):
		self.___keyLockInState = aKeyLockInState
	@LevelCrossingInState.setter
	def LevelCrossingInState(self, *aLevelCrossingInState : LevelCrossingInState):
		self.___levelCrossingInState = aLevelCrossingInState
	@ReleasedForLocalOperation.setter
	def GradieReleasedForLocalOperationntCurve(self, *aReleasedForLocalOperation : EntityILref):
		self.___releasedForLocalOperation = aReleasedForLocalOperation

	def __init__(self):
		self.___activationLock : EntityILref = EntityILref.EntityILref()
		"""reference to any locking device used for activation of the work zone"""
		self.___switchInPosition : SwitchInPosition = SwitchInPosition.SwitchInPosition()
		# @AssociationType Interlocking.SwitchInPosition*
		# @AssociationMultiplicity 0..*
		# """reference to any switch and its position inside or outside the work zone required for use and/or protection"""
		self.___derailerInPosition : DerailerInPosition = DerailerInPosition.DerailerInPosition()
		# @AssociationType Interlocking.DerailerInPosition*
		# @AssociationMultiplicity 0..*
		# """reference to any derailer and its position inside or outside the work zone required for use and/or protection"""
		self.___crossingInPosition : CrossingInPosition = CrossingInPosition.CrossingInPosition()
		# @AssociationType Interlocking.CrossingInPosition*
		# @AssociationMultiplicity 0..*
		# """reference to any movable crossing and its position inside or outside the work zone required for use and/or protection"""
		self.___detectorInState : DetectorInState = DetectorInState.DetectorInState()
		# @AssociationType Interlocking.DetectorInState*
		# @AssociationMultiplicity 0..*
		# """reference to any detector and its state inside or outside the work zone required for use"""
		self.___signalWithAspect : SignalWithAspect = SignalWithAspect.SignalWithAspect()
		# @AssociationType Interlocking.SignalWithAspect*
		# @AssociationMultiplicity 0..*
		# """reference to any signal and its aspect inside or outside the work zone required for use and/or protection"""
		self.___keyLockInState : KeyLockInState = KeyLockInState.KeyLockInState()
		# @AssociationType Interlocking.KeyLockInState*
		# @AssociationMultiplicity 0..*
		# """reference to any key log and its state inside or outside the work zone required for use and/or protection"""
		self.___levelCrossingInState : LevelCrossingInState = LevelCrossingInState.LevelCrossingInState()
		# @AssociationType Interlocking.LevelCrossingInState*
		# @AssociationMultiplicity 0..*
		# """reference to any level crossing and its state inside the work zone required for use"""
		self.___releasedForLocalOperation : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """reference to any element, which is released for local operation, when the work zone is active"""