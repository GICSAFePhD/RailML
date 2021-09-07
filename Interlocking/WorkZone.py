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
	def ActivationLock(self, aActivationLock : EntityILref):	# TODO *aActivationLock
		self.___activationLock = aActivationLock
	@SwitchInPosition.setter
	def SwitchInPosition(self, aSwitchInPosition : SwitchInPosition): # TODO *aSwitchInPosition
		self.___switchInPosition = aSwitchInPosition
	@DerailerInPosition.setter
	def DerailerInPosition(self, aDerailerInPosition : DerailerInPosition): # TODO *aDerailerInPosition
		self.___derailerInPosition = aDerailerInPosition
	@CrossingInPosition.setter
	def CrossingInPosition(self, aCrossingInPosition : CrossingInPosition): # TODO *aCrossingInPosition
		self.___crossingInPosition = aCrossingInPosition
	@DetectorInState.setter
	def DetectorInState(self, aDetectorInState : DetectorInState): # TODO *aDetectorInState
		self.___detectorInState = aDetectorInState
	@SignalWithAspect.setter
	def SignalWithAspect(self, aSignalWithAspect : SignalWithAspect): # TODO *aSignalWithAspect
		self.___signalWithAspect = aSignalWithAspect
	@KeyLockInState.setter
	def KeyLockInState(self, aKeyLockInState : KeyLockInState): # TODO *aKeyLockInState
		self.___keyLockInState = aKeyLockInState
	@LevelCrossingInState.setter
	def LevelCrossingInState(self, aLevelCrossingInState : LevelCrossingInState): # TODO *aLevelCrossingInState
		self.___levelCrossingInState = aLevelCrossingInState
	@ReleasedForLocalOperation.setter
	def ReleasedForLocalOperation(self, aReleasedForLocalOperation : EntityILref): # TODO *aReleasedForLocalOperation
		self.___releasedForLocalOperation = aReleasedForLocalOperation

	def create_ActivationLock(self):
		if self.ActivationLock == None:
			self.ActivationLock = []
		self.ActivationLock.append(EntityILref.EntityILref())
	def create_SwitchInPosition(self):
		if self.SwitchInPosition == None:
			self.SwitchInPosition = []
		self.SwitchInPosition.append(SwitchInPosition.SwitchInPosition())
	def create_DerailerInPosition(self):
		if self.DerailerInPosition == None:
			self.DerailerInPosition = []
		self.DerailerInPosition.append(DerailerInPosition.DerailerInPosition())
	def create_CrossingInPosition(self):
		if self.CrossingInPosition == None:
			self.CrossingInPosition = []
		self.CrossingInPosition.append(CrossingInPosition.CrossingInPosition())
	def create_DetectorInState(self):
		if self.DetectorInState == None:
			self.DetectorInState = []
		self.DetectorInState.append(DetectorInState.DetectorInState())
	def create_SignalWithAspect(self):
		if self.SignalWithAspect == None:
			self.SignalWithAspect = []
		self.SignalWithAspect.append(SignalWithAspect.SignalWithAspect())
	def create_KeyLockInState(self):
		if self.KeyLockInState == None:
			self.KeyLockInState = []
		self.KeyLockInState.append(KeyLockInState.KeyLockInState())
	def create_LevelCrossingInState(self):
		if self.LevelCrossingInState == None:
			self.LevelCrossingInState = []
		self.LevelCrossingInState.append(LevelCrossingInState.LevelCrossingInState())
	def create_ReleasedForLocalOperation(self):
		if self.ReleasedForLocalOperation == None:
			self.ReleasedForLocalOperation = []
		self.ReleasedForLocalOperation.append(EntityILref.EntityILref())

	def __init__(self):
		self.___activationLock : EntityILref = None
		"""reference to any locking device used for activation of the work zone"""
		self.___switchInPosition : SwitchInPosition = None
		# @AssociationType Interlocking.SwitchInPosition*
		# @AssociationMultiplicity 0..*
		# """reference to any switch and its position inside or outside the work zone required for use and/or protection"""
		self.___derailerInPosition : DerailerInPosition = None
		# @AssociationType Interlocking.DerailerInPosition*
		# @AssociationMultiplicity 0..*
		# """reference to any derailer and its position inside or outside the work zone required for use and/or protection"""
		self.___crossingInPosition : CrossingInPosition = None
		# @AssociationType Interlocking.CrossingInPosition*
		# @AssociationMultiplicity 0..*
		# """reference to any movable crossing and its position inside or outside the work zone required for use and/or protection"""
		self.___detectorInState : DetectorInState = None
		# @AssociationType Interlocking.DetectorInState*
		# @AssociationMultiplicity 0..*
		# """reference to any detector and its state inside or outside the work zone required for use"""
		self.___signalWithAspect : SignalWithAspect = None
		# @AssociationType Interlocking.SignalWithAspect*
		# @AssociationMultiplicity 0..*
		# """reference to any signal and its aspect inside or outside the work zone required for use and/or protection"""
		self.___keyLockInState : KeyLockInState = None
		# @AssociationType Interlocking.KeyLockInState*
		# @AssociationMultiplicity 0..*
		# """reference to any key log and its state inside or outside the work zone required for use and/or protection"""
		self.___levelCrossingInState : LevelCrossingInState = None
		# @AssociationType Interlocking.LevelCrossingInState*
		# @AssociationMultiplicity 0..*
		# """reference to any level crossing and its state inside the work zone required for use"""
		self.___releasedForLocalOperation : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """reference to any element, which is released for local operation, when the work zone is active"""