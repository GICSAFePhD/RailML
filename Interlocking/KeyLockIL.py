#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import EntityILref
from Interlocking import LogicalDevice
from typing import List

class KeyLockIL(LogicalDevice):
	"""A device, also known as key lock (de: Schlüsselschalter) situated near the track. It is used to request local control of a (group of) track assets from the interlocking. Commonly, staff requests local control from the interlocking via this device. Once granted, the key can be removed upon which the (group of) track asset is no longer under interlocking control. In reverse, the interlocking takes back control when the key is inserted and staff acknowledged relinquishing control. Note that the lock is a track asset defined in infrastructure namespace. The interlocking reads the state of the lock and returns permission to remove the key, i.e. levelOfControl=fullControl. A combined lock has a master lock that controls a set of slave locks. Slave locks may have to be released in a well-defined sequence."""
	def setHasAutomaticKeyRelease(self, aHasAutomaticKeyRelease : long):
		self.___hasAutomaticKeyRelease = aHasAutomaticKeyRelease

	def getHasAutomaticKeyRelease(self) -> long:
		return self.___hasAutomaticKeyRelease

	def setHasAutomaticKeyLock(self, aHasAutomaticKeyLock : long):
		self.___hasAutomaticKeyLock = aHasAutomaticKeyLock

	def getHasAutomaticKeyLock(self) -> long:
		return self.___hasAutomaticKeyLock

	def setKeyRequestTime(self, aKeyRequestTime : duration):
		self.___keyRequestTime = aKeyRequestTime

	def getKeyRequestTime(self) -> duration:
		return self.___keyRequestTime

	def setKeyAuthoriseTime(self, aKeyAuthoriseTime : duration):
		self.___keyAuthoriseTime = aKeyAuthoriseTime

	def getKeyAuthoriseTime(self) -> duration:
		return self.___keyAuthoriseTime

	def setAcceptsKey(self, aAcceptsKey : EntityILref):
		self._acceptsKey = aAcceptsKey

	def getAcceptsKey(self) -> EntityILref:
		return self._acceptsKey

	def setHasTvdSection(self, *aHasTvdSection : EntityILref*):
		self._hasTvdSection = aHasTvdSection

	def getHasTvdSection(self) -> EntityILref*:
		return self._hasTvdSection

	def setHasSlaveLock(self, aHasSlaveLock : EntityILref):
		self._hasSlaveLock = aHasSlaveLock

	def getHasSlaveLock(self) -> EntityILref:
		return self._hasSlaveLock

	def __init__(self):
		self.___hasAutomaticKeyRelease : long = None
		"""The key of a siding on open line may be released automatically when the related TVD section (trigger) becomes occupied."""
		self.___hasAutomaticKeyLock : long = None
		"""The key may be automatically relocked when returned into the lock. Thus the key can be used only once."""
		self.___keyRequestTime : duration = None
		"""The time period a request for key release is indicated to the operator."""
		self.___keyAuthoriseTime : duration = None
		"""The time period the key release is active after commanded by the operator. Afterwards a not removed key will be automatically relocked again."""
		self._acceptsKey : EntityILref = None
		"""The reference to the particular key used with this master lock."""
		self._hasTvdSection : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The reference to the TVD section related to this master lock. This is especially used for siding key locks on open line."""
		self._hasSlaveLock : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# """reference to a dependent KeyReleaseInstrument"""

