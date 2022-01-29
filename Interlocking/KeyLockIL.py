#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import EntityILref, LogicalDevice
from typing import List, NewType

Long = NewType("Long", int)
Duration = NewType("Duration", int)

class KeyLockIL(LogicalDevice.LogicalDevice):
	"""A device, also known as key lock (de: Schl�sselschalter) situated near the track. It is used to request local control of a (group of) track assets from the interlocking. Commonly, staff requests local control from the interlocking via this device. Once granted, the key can be removed upon which the (group of) track asset is no longer under interlocking control. In reverse, the interlocking takes back control when the key is inserted and staff acknowledged relinquishing control. Note that the lock is a track asset defined in infrastructure namespace. The interlocking reads the state of the lock and returns permission to remove the key, i.e. levelOfControl=fullControl. A combined lock has a master lock that controls a set of slave locks. Slave locks may have to be released in a well-defined sequence."""
	@property
	def HasAutomaticKeyRelease(self) -> Long:
		return self.___hasAutomaticKeyRelease
	@property
	def HasAutomaticKeyLock(self) -> Long:
		return self.___hasAutomaticKeyLock
	@property
	def KeyRequestTime(self) -> Duration:
		return self.___keyRequestTime
	@property
	def KeyAuthoriseTime(self) -> Duration:
		return self.___keyAuthoriseTime
	@property
	def AcceptsKey(self) -> EntityILref:
		return self.___acceptsKey
	@property
	def HasTvdSection(self) -> EntityILref:
		return self.___hasTvdSection
	@property
	def HasSlaveLock(self) -> EntityILref:
		return self.___hasSlaveLock

	@HasAutomaticKeyRelease.setter
	def HasAutomaticKeyRelease(self, aHasAutomaticKeyRelease : Long):
		self.___hasAutomaticKeyRelease = aHasAutomaticKeyRelease
	@HasAutomaticKeyLock.setter
	def HasAutomaticKeyLock(self, aHasAutomaticKeyLock : Long):
		self.___hasAutomaticKeyLock = aHasAutomaticKeyLock
	@KeyRequestTime.setter
	def KeyRequestTime(self, aKeyRequestTime : Duration):
		self.___keyRequestTime = aKeyRequestTime
	@KeyAuthoriseTime.setter
	def KeyAuthoriseTime(self, aKeyAuthoriseTime : Duration):
		self.___keyAuthoriseTime = aKeyAuthoriseTime
	@AcceptsKey.setter
	def AcceptsKey(self, aAcceptsKey : EntityILref):
		self.___acceptsKey = aAcceptsKey
	@HasTvdSection.setter
	def HasTvdSection(self, aHasTvdSection : EntityILref):	#TODO *aHasTvdSection
		self.___hasTvdSection = aHasTvdSection
	@HasSlaveLock.setter
	def HasSlaveLock(self, aHasSlaveLock : EntityILref):
		self.___hasSlaveLock = aHasSlaveLock

	def create_AcceptsKey(self):
		self.AcceptsKey.append(EntityILref.EntityILref())
	def create_HasTvdSection(self):
		if self.HasTvdSection == None:
			self.HasTvdSection = []
		self.HasTvdSection.append(EntityILref.EntityILref())
	def create_HasSlaveLock(self):
		if self.HasSlaveLock == None:
			self.HasSlaveLock = []
		self.HasSlaveLock.append(EntityILref.EntityILref())

	def __init__(self):
		super().__init__()
		self.___hasAutomaticKeyRelease : Long = None
		"""The key of a siding on open line may be released automatically when the related TVD section (trigger) becomes occupied."""
		self.___hasAutomaticKeyLock : Long = None
		"""The key may be automatically relocked when returned into the lock. Thus the key can be used only once."""
		self.___keyRequestTime : Duration = None
		"""The time period a request for key release is indicated to the operator."""
		self.___keyAuthoriseTime : Duration = None
		"""The time period the key release is active after commanded by the operator. Afterwards a not removed key will be automatically relocked again."""
		self.___acceptsKey : EntityILref = None
		"""The reference to the particular key used with this master lock."""
		self.___hasTvdSection : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The reference to the TVD section related to this master lock. This is especially used for siding key locks on open line."""
		self.___hasSlaveLock : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# """reference to a dependent KeyReleaseInstrument"""

