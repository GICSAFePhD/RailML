#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.KeyLockIL import KeyLockIL
from typing import List

class KeyLocksIL(object):
	"""container element for all KeyLockIL elements"""
	def setKeyLockIL(self, *aKeyLockIL : KeyLockIL):
		self._keyLockIL = aKeyLockIL

	def getKeyLockIL(self) -> KeyLockIL:
		return self._keyLockIL

	def __init__(self):
		self._keyLockIL : KeyLockIL = None
		# @AssociationType Interlocking.KeyLockIL*
		# @AssociationMultiplicity 1..*
		# """A device for locking a key which is released from interlocking or by using a master key."""

