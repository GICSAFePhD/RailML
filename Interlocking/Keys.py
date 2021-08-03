#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import Key
from typing import List

class Keys(object):
	"""container element for all Key elements"""
	@property
	def Key(self) -> Key:
		return self.___key
	
	@Key.setter
	def Key(self, aKey : Key):
		self.___key = aKey

	def __init__(self):
		self.___key : Key = Key.Key()
		# @AssociationType Interlocking.Key*
		# @AssociationMultiplicity 1..*
		# """An ancillary element used for operation of a specific locking device."""

