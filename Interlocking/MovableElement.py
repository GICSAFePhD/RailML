#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Interlocking import EntityILref
from RailML.Interlocking import TrackAsset
from typing import List, NewType

Long = NewType("Long", int)
Duration = NewType("Duration", int)
nonNegativeInteger = NewType("nonNegativeInteger", int)

class MovableElement(TrackAsset.TrackAsset):
	"""Abstract element defining the attributes common to movable elements. The movable element refers to TrackAsset, thus creating a link to the IS namespace."""
	# TODO CONTINUE HERE TOMORROW!
	@property
	def MaxThrowTime(self) -> Duration:
		return self.___maxThrowTime
	@property
	def TypicalThrowTime(self) -> Duration:
		return self.___typicalThrowTime
	@property
	def ReturnsToPreferredPosition(self) -> Long:
		return self.______returnsToPreferredPositionid
	@property
	def IsKeyLocked(self) -> Long:
		return self.___isKeyLocked
	@property
	def NumberOfBladeSwitchActuators(self) -> nonNegativeInteger:
		return self.___numberOfBladeSwitchActuators
	@property
	def NumberOfFrogSwitchActuators(self) -> nonNegativeInteger:
		return self.___numberOfFrogSwitchActuators
	@property
	def RefersTo(self) -> EntityILref:
		return self.___refersTo
	@property
	def HasGaugeClearanceMarker(self) -> EntityILref:
		return self.___hasGaugeClearanceMarker
	@property
	def HasTvdSection(self) -> EntityILref:
		return self.___hasTvdSection
	@property
	def ConnectedToPowerSupply(self) -> EntityILref:
		return self.___connectedToPowerSupply
	@property
	def RelatedMovableElement(self) -> EntityILref:
		return self.___relatedMovableElement

	@MaxThrowTime.setter
	def MaxThrowTime(self, aMaxThrowTime : Duration):
		self.___maxThrowTime = aMaxThrowTime
	@TypicalThrowTime.setter
	def TypicalThrowTime(self, aTypicalThrowTime : Duration):
		self.___typicalThrowTime = aTypicalThrowTime
	@ReturnsToPreferredPosition.setter
	def ReturnsToPreferredPosition(self, aReturnsToPreferredPosition : Long):
		self.______returnsToPreferredPositionid = aReturnsToPreferredPosition
	@IsKeyLocked.setter
	def IsKeyLocked(self, aIsKeyLocked : Long):
		self.___isKeyLocked = aIsKeyLocked
	@NumberOfBladeSwitchActuators.setter
	def NumberOfBladeSwitchActuators(self, aNumberOfBladeSwitchActuators : nonNegativeInteger):
		self.___numberOfBladeSwitchActuators = aNumberOfBladeSwitchActuators
	@NumberOfFrogSwitchActuators.setter
	def NumberOfFrogSwitchActuators(self, aNumberOfFrogSwitchActuators : nonNegativeInteger):
		self.___numberOfFrogSwitchActuators = aNumberOfFrogSwitchActuators
	@RefersTo.setter
	def RefersTo(self, aRefersTo : EntityILref): # TODO *aRefersTo
		self.___refersTo = aRefersTo
	@HasGaugeClearanceMarker.setter
	def HasGaugeClearanceMarker(self, aHasGaugeClearanceMarker : EntityILref):
		self.___hasGaugeClearanceMarker = aHasGaugeClearanceMarker
	@HasTvdSection.setter
	def HasTvdSection(self, aHasTvdSection : EntityILref):
		self.___hasTvdSection = aHasTvdSection
	@ConnectedToPowerSupply.setter
	def ConnectedToPowerSupply(self, aConnectedToPowerSupply : EntityILref):
		self.___connectedToPowerSupply = aConnectedToPowerSupply
	@RelatedMovableElement.setter
	def RelatedMovableElement(self, aRelatedMovableElement : EntityILref):
		self.___relatedMovableElement = aRelatedMovableElement

	def create_RefersTo(self):
		if self.RefersTo == None:
			self.RefersTo = []
		self.RefersTo.append(EntityILref.EntityILref())
	def create_HasGaugeClearanceMarker(self):
		if self.HasGaugeClearanceMarker == None:
			self.HasGaugeClearanceMarker = []
		self.HasGaugeClearanceMarker.append(EntityILref.EntityILref())
	def create_HasTvdSection(self):
		if self.HasTvdSection == None:
			self.HasTvdSection = []
		self.HasTvdSection.append(EntityILref.EntityILref())
	def create_ConnectedToPowerSupply(self):
		if self.ConnectedToPowerSupply == None:
			self.ConnectedToPowerSupply = []
		self.ConnectedToPowerSupply.append(EntityILref.EntityILref())
	def create_RelatedMovableElement(self):
		if self.RelatedMovableElement == None:
			self.RelatedMovableElement = []
		self.RelatedMovableElement.append(EntityILref.EntityILref())

	def __init__(self):
		super().__init__()
		self.___maxThrowTime : Duration = None
		"""Maximum time in milliseconds during which the IL can drive the element. If it has not reached end-position before this timer expires, the interlocking stops throwing as to prevent damage."""
		self.___typicalThrowTime : Duration = None
		"""typical throw time is the average time it takes between the moment the IL receives the call and the element reaches the new position. Switch throwing adds a delay to route setting that is of great interest to the use case simulation. For this purpose, we add an attribute typicalThrowTime that allows capacity planners to estimate the influence of slow throwing switches on train traffic. Note that this excludes controller (OCS) processing time and communication between controller (OCS) and interlocking."""
		self.___returnsToPreferredPosition : Long = None
		"""The automatic normalisation attribute is closely related to the preferred position. Whether or not the IL returns the element to its preferred position depends on this parameter. E.g. a derailer that is modelled as ... preferredPosition=engaged autoNormalisation=true ... will return to its engaged position when released. A switch modelled as preferredPosition=right autoNormalisation=false... will not automatically return to the right position when released. This combination of attributes is useful for geographical interlockings that automatically determine the preferred routes given the preferred position of intervening switches."""
		self.___isKeyLocked : Long = None
		"""One of boolean true or false. True means that the switch is clamped either mechanically or by any electric or electronic means. The interlocking shall never attempt to throw a clamped switch."""
		self.___numberOfBladeSwitchActuators : nonNegativeInteger = None
		"""number of switch actuators controlled from interlocking to throw the switch blades, 0 means no direct operation from the interlocking"""
		self.___numberOfFrogSwitchActuators : nonNegativeInteger = None
		"""number of switch actuators controlled from interlocking to throw the frog nose(s), 0 means no movable frog"""
		self.___refersTo : EntityILref = None
		"""Reference to the physical movable element in the infrastructure."""
		self.___hasGaugeClearanceMarker : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# """the reference to any gauge clearance marker in infrastructure"""
		self.___hasTvdSection : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# """Reference to the underlying TVD section of the movable element"""
		self.___connectedToPowerSupply : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# """relation to power supply for controlling the number of simultaneously switched switch actuators"""
		self.___relatedMovableElement : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """reference to other movable element in case of single/double slip switch or coupled switch"""