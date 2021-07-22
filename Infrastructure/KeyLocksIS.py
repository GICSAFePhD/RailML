#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import KeyLockIS
from typing import List

class KeyLocksIS(object):
	@property
	def KeyLockIS(self) -> KeyLockIS:
		return self.___keyLockIS
	
	@KeyLockIS.setter
	def KeyLockIS(self, aKeyLockIS : KeyLockIS):
		self.___keyLockIS = aKeyLockIS

	def __init__(self):
		self.___keyLockIS : KeyLockIS = KeyLockIS.KeyLockIS()
		# @AssociationType Infrastructure.KeyLockIS*
		# @AssociationMultiplicity 1..*

