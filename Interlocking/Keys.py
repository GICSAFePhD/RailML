#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.Key import Key
from typing import List

class Keys(object):
	"""container element for all Key elements"""
	def setKey(self, *aKey : Key):
		self._key = aKey

	def getKey(self) -> Key:
		return self._key

	def __init__(self):
		self._key : Key = None
		# @AssociationType Interlocking.Key*
		# @AssociationMultiplicity 1..*
		# """An ancillary element used for operation of a specific locking device."""

