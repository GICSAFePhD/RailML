#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import KeyLockIS
from typing import List

class KeyLocksIS(object):
	def setKeyLockIS(self, *aKeyLockIS : KeyLockIS*):
		self._keyLockIS = aKeyLockIS

	def getKeyLockIS(self) -> KeyLockIS*:
		return self._keyLockIS

	def __init__(self):
		self._keyLockIS : KeyLockIS = None
		# @AssociationType Infrastructure.KeyLockIS*
		# @AssociationMultiplicity 1..*

