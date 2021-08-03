#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import KeyLockIL
from typing import List

class KeyLocksIL(object):
	"""container element for all KeyLockIL elements"""
	@property
	def KeyLockIL(self) -> KeyLockIL:
		return self.___keyLockIL
	
	@KeyLockIL.setter
	def KeyLockIL(self, *aKeyLockIL : KeyLockIL):
		self.___keyLockIL = aKeyLockIL

	def __init__(self):
		self.___keyLockIL : KeyLockIL = KeyLockIL.KeyLockIL()
		# @AssociationType Interlocking.KeyLockIL*
		# @AssociationMultiplicity 1..*
		# """A device for locking a key which is released from interlocking or by using a master key."""

