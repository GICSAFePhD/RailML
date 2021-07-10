#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from Interlocking import EntityILref
from Interlocking import TrackAsset
from typing import List

class MovableElement(TrackAsset):
	"""Abstract element defining the attributes common to movable elements. The movable element refers to TrackAsset, thus creating a link to the IS namespace."""
	__metaclass__ = ABCMeta
	@classmethod
	def setMaxThrowTime(self, aMaxThrowTime : duration):
		self.___maxThrowTime = aMaxThrowTime

	@classmethod
	def getMaxThrowTime(self) -> duration:
		return self.___maxThrowTime

	@classmethod
	def setTypicalThrowTime(self, aTypicalThrowTime : duration):
		self.___typicalThrowTime = aTypicalThrowTime

	@classmethod
	def getTypicalThrowTime(self) -> duration:
		return self.___typicalThrowTime

	@classmethod
	def setReturnsToPreferredPosition(self, aReturnsToPreferredPosition : long):
		self.___returnsToPreferredPosition = aReturnsToPreferredPosition

	@classmethod
	def getReturnsToPreferredPosition(self) -> long:
		return self.___returnsToPreferredPosition

	@classmethod
	def setIsKeyLocked(self, aIsKeyLocked : long):
		self.___isKeyLocked = aIsKeyLocked

	@classmethod
	def getIsKeyLocked(self) -> long:
		return self.___isKeyLocked

	@classmethod
	def setNumberOfBladeSwitchActuators(self, aNumberOfBladeSwitchActuators : nonNegativeInteger):
		self.___numberOfBladeSwitchActuators = aNumberOfBladeSwitchActuators

	@classmethod
	def getNumberOfBladeSwitchActuators(self) -> nonNegativeInteger:
		return self.___numberOfBladeSwitchActuators

	@classmethod
	def setNumberOfFrogSwitchActuators(self, aNumberOfFrogSwitchActuators : nonNegativeInteger):
		self.___numberOfFrogSwitchActuators = aNumberOfFrogSwitchActuators

	@classmethod
	def getNumberOfFrogSwitchActuators(self) -> nonNegativeInteger:
		return self.___numberOfFrogSwitchActuators

	@classmethod
	def setRefersTo(self, *aRefersTo : EntityILref*):
		self._refersTo = aRefersTo

	@classmethod
	def getRefersTo(self) -> EntityILref*:
		return self._refersTo

	@classmethod
	def setHasGaugeClearanceMarker(self, aHasGaugeClearanceMarker : EntityILref):
		self._hasGaugeClearanceMarker = aHasGaugeClearanceMarker

	@classmethod
	def getHasGaugeClearanceMarker(self) -> EntityILref:
		return self._hasGaugeClearanceMarker

	@classmethod
	def setHasTvdSection(self, aHasTvdSection : EntityILref):
		self._hasTvdSection = aHasTvdSection

	@classmethod
	def getHasTvdSection(self) -> EntityILref:
		return self._hasTvdSection

	@classmethod
	def setConnectedToPowerSupply(self, aConnectedToPowerSupply : EntityILref):
		self._connectedToPowerSupply = aConnectedToPowerSupply

	@classmethod
	def getConnectedToPowerSupply(self) -> EntityILref:
		return self._connectedToPowerSupply

	@classmethod
	def setRelatedMovableElement(self, aRelatedMovableElement : EntityILref):
		self._relatedMovableElement = aRelatedMovableElement

	@classmethod
	def getRelatedMovableElement(self) -> EntityILref:
		return self._relatedMovableElement

	@classmethod
	def __init__(self):
		self.___maxThrowTime : duration = None
		"""Maximum time in milliseconds during which the IL can drive the element. If it has not reached end-position before this timer expires, the interlocking stops throwing as to prevent damage."""
		self.___typicalThrowTime : duration = None
		"""typical throw time is the average time it takes between the moment the IL receives the call and the element reaches the new position. Switch throwing adds a delay to route setting that is of great interest to the use case simulation. For this purpose, we add an attribute typicalThrowTime that allows capacity planners to estimate the influence of slow throwing switches on train traffic. Note that this excludes controller (OCS) processing time and communication between controller (OCS) and interlocking."""
		self.___returnsToPreferredPosition : long = None
		"""The automatic normalisation attribute is closely related to the preferred position. Whether or not the IL returns the element to its preferred position depends on this parameter. E.g. a derailer that is modelled as ... preferredPosition=engaged autoNormalisation=true ... will return to its engaged position when released. A switch modelled as preferredPosition=right autoNormalisation=false... will not automatically return to the right position when released. This combination of attributes is useful for geographical interlockings that automatically determine the preferred routes given the preferred position of intervening switches."""
		self.___isKeyLocked : long = None
		"""One of boolean true or false. True means that the switch is clamped either mechanically or by any electric or electronic means. The interlocking shall never attempt to throw a clamped switch."""
		self.___numberOfBladeSwitchActuators : nonNegativeInteger = None
		"""number of switch actuators controlled from interlocking to throw the switch blades, 0 means no direct operation from the interlocking"""
		self.___numberOfFrogSwitchActuators : nonNegativeInteger = None
		"""number of switch actuators controlled from interlocking to throw the frog nose(s), 0 means no movable frog"""
		self._refersTo : EntityILref = None
		"""Reference to the physical movable element in the infrastructure."""
		self._hasGaugeClearanceMarker : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# """the reference to any gauge clearance marker in infrastructure"""
		self._hasTvdSection : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# """Reference to the underlying TVD section of the movable element"""
		self._connectedToPowerSupply : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# """relation to power supply for controlling the number of simultaneously switched switch actuators"""
		self._relatedMovableElement : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """reference to other movable element in case of single/double slip switch or coupled switch"""

